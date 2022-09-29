from Crypto.Cipher import AES
from Crypto.Cipher import DES3
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

#Global variables for Layer 1
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

def main():
    plaintext = b'tanvi is hot'
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