from config import Config
from entry import Entry
from key import Key
from encryption import Encryption
from utils import Utils

import hashlib

def checkPassword(path,user_password):
    data = Utils.readJson(path)
    password = data["MasterPassword"]
    if password == user_password:
        return True
    else:
        return False

def setMasterPassword():
    password = str(input("Please enter your initial master password: "))
    if Utils.question(password):
        return password
    else:
        setMasterPassword()

def hashPassword(password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed

def main():
    print("---- Password Manager ----")
    config = Config()
    if config.checkConfigFile():
        config_path = config.getConfigPath()
        while True:
            password = str(input("Enter your master password: "))
            userPassword = hashPassword(password)
            if checkPassword(config_path,userPassword):
                print("Your password is correct.")
                break
            else:
                print("Password incorrect.")
                return 0
    else:
        config.createInitialConfig()
        hashedPassword = hashPassword(setMasterPassword())
        Utils.updateValJson(config.getConfigPath(),"MasterPassword",hashedPassword)


if __name__ == "__main__":
    main()