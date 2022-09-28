from Crypto.Cipher import AES
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def main():
    plaintext = b'tanvi is cool'
    layer1(plaintext)

def layer1(plaintext):
    file_out = open("encrypted_data.bin", "wb")

    recipient_key = RSA.import_key(open("receiver.pem").read())
    session_key = get_random_bytes(16)

    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(plaintext)
    [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
    file_out.close()
    layer2(ciphertext)

# Global variables for Layer 2
key2 = get_random_bytes(16)
e_cipher = AES.new(key2, AES.MODE_EAX)
d_cipher = AES.new(key2, AES.MODE_EAX, e_cipher.nonce)

# Global variables for Layer 3
key3 = get_random_bytes(16)
E_cipher = DES3.new(key3, DES3.MODE_EAX)
D_cipher = DES3.new(key3, DES3.MODE_EAX, E_cipher.nonce)

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
    layer1_D(plaintext)

def layer1_D(ciphertext):
    file_in = open("encrypted_data.bin", "rb")

    private_key = RSA.import_key(open("private.pem").read())

    enc_session_key, nonce, tag, ciphertext = \
    [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

    # Decrypt the session key with the private RSA key
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    # Decrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    plaintext = cipher_aes.decrypt_and_verify(ciphertext, tag)
    print(plaintext)

main()