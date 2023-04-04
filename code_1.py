from PIL import Image
import lzma

from Crypto.Cipher import AES, DES3, PKCS1_OAEP
from Crypto.PublicKey import RSA
from stegano import lsbset, lsb
from stegano.lsbset import generators


# Randomizer byte number function
def get_bytes(n):
    random_number = 1000
    return random_number.to_bytes(n, "big")


# Global Variables for Layer 1 - RSA
rsa_public_key = RSA.import_key(open("keys/rsa_public_key.pem").read())
rsa_private_key = RSA.import_key(open("keys/rsa_private_key.pem").read())
rsa_encryptor = PKCS1_OAEP.new(rsa_public_key, randfunc=get_bytes)
rsa_decryptor = PKCS1_OAEP.new(rsa_private_key)

# Global Variables for Layer 2 - AES
with open("keys/aes_key.pem", "rb") as p:
    aes_key = p.read()
aes_encryptor = AES.new(aes_key, AES.MODE_EAX, nonce=b"123456")
aes_decryptor = AES.new(aes_key, AES.MODE_EAX, aes_encryptor.nonce)

# Global Variables for Layer 3 - 3DES
with open("keys/des3_key.pem", "rb") as p:
    des_key = p.read()
des_encryptor = DES3.new(des_key, DES3.MODE_EAX, nonce=b"123456")
des_decryptor = DES3.new(des_key, DES3.MODE_EAX, des_encryptor.nonce)

# Double Encryption Function


def encrypt(plaintext):

    # Generating ciphertext by passing through layer 1 using plaintext as input
    print(len(plaintext[0:10]), plaintext[0:10])
    ciphertext = rsa_encryptor.encrypt(plaintext[0:10])
    print(len(ciphertext))
    print('\nLayer 1 RSA Ciphertext: ')
    # print(ciphertext)

    # Generating ciphertext by passing through layer 2 using ciphertext from layer 1 as input
    ciphertext = aes_encryptor.encrypt(b"".join([ciphertext, plaintext]))
    print('\n\nLayer 2 AES Ciphertext: ')
    # print(ciphertext)

    # Generating ciphertext by passing through layer 3 using ciphertext from layer 2 as input
    ciphertext = des_encryptor.encrypt(ciphertext)
    print('\n\nLayer 3 3DES Ciphertext: ')
    # print(ciphertext)

    # Returning Ciphertext to called function
    return ciphertext


# Embedding text in a cover image using LSB technique
def hide(ciphertext, im1, im1Secr1):

    # Embedding ciphertext using Steganography using LSB technique
    embedded_image = lsb.hide(im1, str(ciphertext))

    # Saving the image as coverImageSecret.png with the embedded ciphertext
    embedded_image.save(im1Secr1)


# Revealing hidden text from the steganographic image
def reveal(im1Secr1):

    # Revealing the hidden ciphertext from coverImageSecret.png
    ciphertext = lsb.reveal(im1Secr1)

    # Encoding the ciphertext to Byte format for decryption
    ciphertext = (
        ciphertext[2:-1].encode().decode("unicode_escape").encode("raw_unicode_escape")
    )

    return ciphertext


# Double Decryption Function
def decrypt(ciphertext):

    # Generating plaintext by passing through layer 3 using ciphertext as input
    plaintext = des_decryptor.decrypt(ciphertext)

    # Generating plaintext by passing through layer 2 using plaintext from layer 3 as input
    plaintext = aes_decryptor.decrypt(plaintext)

    rest = plaintext[129:]
    print(plaintext[-9:], len(plaintext[-9:]))
    # Generating plaintext by passing through layer 1 using plaintext from layer 2 as input
    plaintext = rsa_decryptor.decrypt(plaintext[0:128])

    plaintext = plaintext + rest
    print(len(plaintext))

    # Returning plaintext to called function
    return plaintext


# Main Function
def main(plaintext, im1, im1Secr1):

    # Receiving Plaintext from User
    # plaintext = input("Enter plaintext: ")
    print("Plaintext: "+plaintext+"\n")
    plaintext = bytes(plaintext, "utf-8")

    # Compressing plaintext before Double Encryption
    # plaintext = lzma.compress(plaintext)

    # Encrypting the plaintext using Double Encryption
    ciphertext = encrypt(plaintext)

    # Hiding the Double Encrypted ciphertext in a cover image
    hide(ciphertext, im1, im1Secr1)

    # Calling reveal() to reveal the hidden ciphertext in the coverImageSecret.png
    revealed_ciphertext = reveal(im1Secr1)

    # Decrypting the obtained ciphertext from the steganographic image
    decrypted_plaintext = decrypt(revealed_ciphertext)
    # print('\n\Compressed Output :')
    # print(decrypted_plaintext)

    # Decompressing the obtained plaintext after Decryption
    # decrypted_plaintext = lzma.decompress(decrypted_plaintext)
    decrypted_plaintext = decrypted_plaintext.decode("utf-8")

    # Printing Plaintext after Double Decryption
    print('\n\nFinal Output :')
    print(decrypted_plaintext)


# Calling the main function
im1 = "images/tulips.png"
im1Secr1 = "images/tulipsSecret1.png"
im1Secr2 = "images/tulipsSecret2.png"
im1Secr3 = "images/tulipsSecret3.png"
im1Secr4 = "images/tulipsSecret4.png"
im1Secr5 = "images/tulipsSecret5.png"
# strin = "LztxSwF)KCatW@KD]rR;!Hh4CA.=BE9PTk+MU;54?8_GR)+i:3-F{uT8t*FYh#j%$_4R{j{({ht=yWKGkBH##_@&@wR}&cA]]H9?"
strin = "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"


img = Image.open(im1)

width = img.width
height = img.height

# display width and height
print("pixels * 3: ", width * height * 3)
print("length", len(strin.encode('utf-8')) * 8)

# main("M5Csn",im1,im1Secr1)
# main("10TkfR2iWg",im1,im1Secr2)
# main("bvrod1ElJRD8T6H",im1,im1Secr3)
# main("MiMvlXX4vMD9WfssukC2",im1,im1Secr4)
main(strin, im1, im1Secr1)
