import os

from utils import Utils
class Config:
    def __init__(self):
        self.__configPath = os.path.join(os.getcwd(),"config.json")
        self.__entryPath = os.path.join(os.getcwd(),"entry.json")
        self.__keyPath = os.path.join(os.getcwd(),"key.key")
        self.__masterPassword = ""

    def checkConfigFile(self):
        return os.path.exists(self.__configPath)

    def createInitialConfig(self):
        data = {
            "ConfigPath": self.__configPath,
            "EntryPath": self.__entryPath,
            "KeyPath": self.__keyPath,
            "MasterPassword": self.__masterPassword,
            "FirstRun": True
        }
        Utils.writeJson(self.__configPath,data)

    def getConfigPath(self):
        return Utils.getValJson(self.__configPath,"ConfigPath")

    def getEntryPath(self):
        return Utils.getValJson(self.__configPath,"EntryPath")

    def getKeyPath(self):
        return Utils.getValJson(self.__configPath,"KeyPath")

    def getMasterPassword(self):
        return Utils.getValJson(self.__configPath,"MasterPassword")

    def getFirstRun(self):
        return Utils.getValJson(self.__configPath,"FirstRun")

    def setFirstRun(self,firstRun):
        Utils.updateValJson(self.__configPath,"FirstRun",firstRun)