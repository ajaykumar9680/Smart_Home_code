from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class RSAIntegration:
    def __init__(self):
        # Load public and private keys
        self.private_key = RSA.generate(2048)
        self.public_key = self.private_key.publickey()

    def encrypt_data(self, data):
        cipher = PKCS1_OAEP.new(self.public_key)
        encrypted_data = cipher.encrypt(data.encode())
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        cipher = PKCS1_OAEP.new(self.private_key)
        decrypted_data = cipher.decrypt(encrypted_data)
        return decrypted_data.decode()
