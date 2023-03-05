import lzma

from Crypto.Cipher import AES, DES3, PKCS1_OAEP
from Crypto.PublicKey import RSA
from stegano import lsbset
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
    ciphertext = rsa_encryptor.encrypt(plaintext)
    print('\nLayer 1 RSA Ciphertext: ')
    print(ciphertext)

    # Generating ciphertext by passing through layer 2 using ciphertext from layer 1 as input
    ciphertext = aes_encryptor.encrypt(ciphertext)
    print('\n\nLayer 2 AES Ciphertext: ')
    print(ciphertext)

    # Generating ciphertext by passing through layer 3 using ciphertext from layer 2 as input
    ciphertext = des_encryptor.encrypt(ciphertext)
    print('\n\nLayer 3 3DES Ciphertext: ')
    print(ciphertext)

    # Returning Ciphertext to called function
    return ciphertext


# Embedding text in a cover image using LSB technique
def hide(ciphertext,im1,im1Secr1):

    # Embedding ciphertext using Steganography using LSB technique
    embedded_image = lsbset.hide(im1, str(ciphertext), generators.eratosthenes())

    # Saving the image as coverImageSecret.png with the embedded ciphertext
    embedded_image.save(im1Secr1)


# Revealing hidden text from the steganographic image
def reveal(im1Secr1):

    # Revealing the hidden ciphertext from coverImageSecret.png
    ciphertext = lsbset.reveal(im1Secr1, generators.eratosthenes())

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

    # Generating plaintext by passing through layer 1 using plaintext from layer 2 as input
    plaintext = rsa_decryptor.decrypt(plaintext)

    # Returning plaintext to called function
    return plaintext


# Main Function
def main(plaintext,im1,im1Secr1):

    # Receiving Plaintext from User
    # plaintext = input("Enter plaintext: ")
    print("Plaintext: "+plaintext+"\n")
    plaintext = bytes(plaintext, "utf-8")

    # Compressing plaintext before Double Encryption
    plaintext = lzma.compress(plaintext)

    # Encrypting the plaintext using Double Encryption
    ciphertext = encrypt(plaintext)

    # Hiding the Double Encrypted ciphertext in a cover image
    hide(ciphertext,im1,im1Secr1)

    # Calling reveal() to reveal the hidden ciphertext in the coverImageSecret.png
    revealed_ciphertext = reveal(im1Secr1)

    # Decrypting the obtained ciphertext from the steganographic image
    decrypted_plaintext = decrypt(revealed_ciphertext)
    # print('\n\Compressed Output :')
    # print(decrypted_plaintext)

    # Decompressing the obtained plaintext after Decryption
    decrypted_plaintext = lzma.decompress(decrypted_plaintext)
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

# main("M5Csn",im1,im1Secr1)
# main("10TkfR2iWg",im1,im1Secr2)
# main("bvrod1ElJRD8T6H",im1,im1Secr3)
# main("MiMvlXX4vMD9WfssukC2",im1,im1Secr4)
main("uejgbhlOUWEGHOGHRJGHALJGHKJHLjhljshlgjshdgkiyud",im1,im1Secr5)
