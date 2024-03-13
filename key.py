import os
import json

from utils import Utils
from cryptography.fernet import Fernet

class Key:
    def __init__(self):
        config_data = Utils.readJson(os.path.join(os.getcwd(), "config.json"))
        self.__keyPath = config_data["KeyPath"]
        self.__key = Utils.readBinary(self.__keyPath)

    @staticmethod
    def generateKey():
        return Fernet.generate_key()

    def checkKey(self):
        return os.path.exists(self.__keyPath)

    def getKey(self):
        return self.__key

    def setKey(self, key):
        self.__key = key

    def writeKey(self):
        Utils.writeBinary(self.__keyPath, self.__key)
