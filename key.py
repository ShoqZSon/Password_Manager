import os
import json

from utils import Utils
from cryptography.fernet import Fernet

class Key:
    def __init__(self,configPath):
        config_data = Utils.readJson(configPath)
        self.__keyPath = config_data["KeyPath"]
        self.__key = ""

    def loadKey(self):
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

    def writeKey(self,keyPath):
        Utils.writeBinary(keyPath, self.__key)
