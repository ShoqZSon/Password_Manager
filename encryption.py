from cryptography.fernet import Fernet
from utils import Utils#
import json

class Encryption:
    def __init__(self,configPath):
        config_data = Utils.readJson(configPath)
        key_path = config_data["KeyPath"]
        self.__key = Utils.readBinary(key_path)

    def encrypt(self, plaintext):
        cipherSuite = Fernet(self.__key)

        encryptedList = cipherSuite.encrypt(plaintext.encode('utf-8'))

        return encryptedList

    def decrypt(self, encryptedText):
        cipherSuite = Fernet(self.__key)
        decryptedText = cipherSuite.decrypt(encryptedText)
        decryptedList = decryptedText.decode('utf-8')

        return decryptedList