from Crypto.Cipher import AES
from Crypto.Cipher import DES3
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import sys
import codecs
import numpy as np
from PIL import Image
np.set_printoptions(threshold=sys.maxsize)

# Global variables for Layer 1
public_key = RSA.import_key(open("keys/layer1Public.pem").read())
private_key = RSA.import_key(open("keys/layer1Private.pem").read())
cipher_e = PKCS1_OAEP.new(public_key)
cipher_d = PKCS1_OAEP.new(private_key)

# Global variables for Layer 2
with open('keys/layer2.pem', 'rb') as p:
    key2 = p.read()
e_cipher = AES.new(key2, AES.MODE_EAX)
d_cipher = AES.new(key2, AES.MODE_EAX, e_cipher.nonce)

# Global variables for Layer 3
with open('keys/layer2.pem', 'rb') as p:
    key3 = p.read()
E_cipher = DES3.new(key3, DES3.MODE_EAX)
D_cipher = DES3.new(key3, DES3.MODE_EAX, E_cipher.nonce)

# For steganography
src = "input.png"
dest = "output.png"

def main():
    with open('plaintext.txt', 'rb') as p:
        plaintext = p.read()
    layer1(plaintext)

def layer1(plaintext):

    # Generating ciphertext which serves as input to layer 2
    ciphertext = cipher_e.encrypt(plaintext)
    # Sending ciphertext to Layer 2 for Encryption
    layer2(ciphertext)

# Layer 2 - Encryption using AES-128
def layer2(plaintext):

    # Generating ciphertext which serves as input to layer 3 
    ciphertext = e_cipher.encrypt(plaintext)
    # Sending Ciphertext to Layer 3 for Encryption
    layer3(ciphertext)

# Layer 3 - Encryption using DES3
def layer3(plaintext):

    # Generating Ciphertext
    ciphertext = E_cipher.encrypt(plaintext)
    # Sending Ciphertext to Layer 3 for Decryption
    # layer3_D(ciphertext)
    print(ciphertext)
    StegEncode(src,ciphertext, dest)

#encoding function
def StegEncode(src, message, dest):

    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4

    total_pixels = array.size//n

    print(type(message))
    message = codecs.decode(message)
    message += "$t3g0"
    b_message = ''.join([format(ord(i), "08b") for i in message])
    req_pixels = len(b_message)

    if req_pixels > total_pixels:
        print("ERROR: Need larger file size")

    else:
        index=0
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                    index += 1

        array=array.reshape(height, width, n)
        enc_img = Image.fromarray(array.astype('uint8'), img.mode)
        enc_img.save(dest, 'png')
        print("Image StegEncoded Successfully")


#decoding function
def StegDecode(src):

    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4

    total_pixels = array.size//n

    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])

    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    message = ""
    for i in range(len(hidden_bits)):
        if message[-5:] == "$t3g0":
            break
        else:
            message += chr(int(hidden_bits[i], 2))
    if "$t3g0" in message:
        print("Hidden Message:", message[:-5])
    else:
        print("No Hidden Message Found")
    ciphertext = message[:-5].encode('utf-8')
    layer3_D(ciphertext)


# Layer 3 - Decryption using DES3
def layer3_D(ciphertext):

    # Decrypting Data received after 3 layers of Encryption
    plaintext =  D_cipher.decrypt(ciphertext)
    # Sending Message to Layer 2 for Decryption
    layer2_D(plaintext)

# Layer 2 - Decryption using AES
def layer2_D(ciphertext):

    # Decrypting Data received from previous layer
    plaintext = d_cipher.decrypt(ciphertext)
    # Sending Message to Layer 1 for Decryption
    layer1_D(plaintext)

def layer1_D(ciphertext):

    # Decrypting data received from previous layer
    plaintext = cipher_d.decrypt(ciphertext)
    # Final plaintext
    print(plaintext)

main()