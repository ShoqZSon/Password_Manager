import os

from utils import Utils
class Entry:
    def __init__(self,configPath):
        config_data = Utils.readJson(configPath)
        self.__entryPath = config_data["EntryPath"]

    def createInitialEntryFile(self):
        data = {
            "Entries": [],
            "Encrypted": False
        }
        Utils.writeJson(self.__entryPath, data)

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
        if self.__checkEntryFile():
            return Utils.getValJson(self.__entryPath, "Entries")
        else:
            raise FileNotFoundError("")

    def getEncrypted(self):
        return bool(Utils.getValJson(self.__entryPath, "Encrypted"))

    def setEntries(self, entries):
        Utils.updateValJson(self.__entryPath, "Entries",entries)

    def setEncrypted(self, encrypted):
        if isinstance(encrypted, bool):
            Utils.updateValJson(self.__entryPath, "Encrypted",encrypted)
        else:
            print("Argument has to be a boolean value")
