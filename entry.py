import os
import json

from utils import Utils
class Entry:
    def __init__(self,configPath):
        config_data = Utils.readJson(configPath)
        self.__entryPath = config_data["entry.json"]

    def __checkEntryFile(self):
        return os.path.exists(self.__entryPath)

    def createEntry(self,usage,password):
        data = Utils.readJson(self.__entryPath)

        data["Entries"].append({
            "Usage":usage,
            "Password":password
        })

        Utils.writeJson(self.__entryPath, data)

    def createInitialEntry(self):
        data = {
            "Entries": [],
            "Encrypted": False
        }
        Utils.writeJson(self.__entryPath, data)

    def getEntries(self):
        entries = Utils.getValJson(self.__entryPath, "Entries")
        return entries

    def getEncrypted(self):
        encrypted = Utils.getValJson(self.__entryPath, "Encrypted")
        return encrypted
