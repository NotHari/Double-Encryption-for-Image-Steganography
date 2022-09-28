from Crypto.Cipher import AES
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

# Global variables for Layer 2
key2 = get_random_bytes(16)
e_cipher = AES.new(key2, AES.MODE_EAX)
d_cipher = AES.new(key2, AES.MODE_EAX, e_cipher.nonce)

# Global variables for Layer 3
key3 = get_random_bytes(16)
E_cipher = DES3.new(key3, DES3.MODE_EAX)
D_cipher = DES3.new(key3, DES3.MODE_EAX, E_cipher.nonce)

def main():
    plaintext = b'tanvi is cool'
    layer2(plaintext)

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
    #Final Plaintext
    print(plaintext)

main()