from cryptography.fernet import Fernet
from utils import Utils

class Encryption:
    def __init__(self,configPath):
        config_data = Utils.readJson(configPath)
        key_path = config_data["KeyPath"]
        self.__key = Utils.readBinary(key_path)

    def encrypt(self, plaintext):
        cipher_suite = Fernet(self.__key)
        encrypted_text = cipher_suite.encrypt(plaintext.encode())

        return encrypted_text

    def decrypt(self, encrypted_text):
        cipher_suite = Fernet(self.__key)
        decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
        return decrypted_text