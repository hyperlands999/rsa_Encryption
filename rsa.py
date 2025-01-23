from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

class RSATool:
    def __init__(self, key_size=2048):
        self.key = RSA.generate(key_size)
        self.private_key = self.key.export_key()
        self.public_key = self.key.publickey().export_key()

    def encrypt(self, message, public_key):
        rsa_key = RSA.import_key(public_key)
        cipher = PKCS1_OAEP.new(rsa_key)
        encrypted_message = cipher.encrypt(message.encode())
        return base64.b64encode(encrypted_message).decode()

    def decrypt(self, encrypted_message):
        encrypted_message = base64.b64decode(encrypted_message.encode())
        rsa_key = RSA.import_key(self.private_key)
        cipher = PKCS1_OAEP.new(rsa_key)
        decrypted_message = cipher.decrypt(encrypted_message)
        return decrypted_message.decode()