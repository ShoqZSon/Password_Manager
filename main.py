from config import Config
from entry import Entry
from key import Key
from encryption import Encryption
from utils import Utils

import time
import hashlib
import string
import random

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

def setUsage():
    while True:
        usage = str(input("Enter the passwords usage: "))
        if Utils.question(usage):
            break

    return usage

def setPasswordLength():
    while True:
        passwordLength = int(input("Enter the password length: "))
        if 9 < passwordLength < 21:
            if Utils.question(passwordLength):
                return passwordLength
            else:
                setPasswordLength()
        else:
            print("Password length has to be between 10 and 20 (inclusive)")

def setPassword(passwordLength):
    characters = string.ascii_letters + string.digits + string.punctuation
    random.shuffle(list(characters))

    passwordList = [""] * passwordLength
    while True:
        for _ in range(passwordLength):
            passwordList.append(random.choice(characters))

        password = "".join(passwordList)
        if Utils.question(password):
            return password
        else:
            setPassword()

def main():
    print("---- Password Manager ----")
    config = Config()
    if config.checkConfigFile():
        configPath = config.getConfigPath()
        while True:
            password = str(input("Enter your master password: "))
            userPassword = hashPassword(password)
            if checkPassword(configPath,userPassword):
                print("Your password is correct.")
                break
            else:
                print("Password incorrect.")
                return 0
        entry = Entry(configPath)
    else:
        config.createInitialConfig()
        configPath = config.getConfigPath()
        hashedPassword = hashPassword(setMasterPassword())
        Utils.updateValJson(configPath,"MasterPassword",hashedPassword)

        key = Key(configPath)
        key_k = key.generateKey()
        key.setKey(key_k)
        key.writeKey(config.getKeyPath())

        entry = Entry(configPath)
        entry.createInitialEntryFile()

    encrypt = Encryption(configPath)

    print("Options:")
    print("1. Generate a new entry")
    print("2. Show stored passwords")
    print("3. Exit")
    while True:
        option = int(input("Enter your option: "))
        if option == 1:
            if config.getFirstRun():
                usage = setUsage()
                password = setPassword(setPasswordLength())

                entry.createEntry(usage,password)
                entries = entry.getEntries()
                time.sleep(15)
                encryptedEntries = encrypt.encrypt(entries)
                print(encryptedEntries)
                # setting encrypted entries throws a TypeError
                # TODO: need setEntries method for setting the binary data as string or json format
                entry.setEntries(encryptedEntries)
                config.setFirstRun(False)
            elif entry.getEncrypted() and not config.getFirstRun():
                # get the whole entry data
                entries = entry.getEntries()
                # decrypt the data
                decryptedEntries = encrypt.decrypt(entries)
                # write the decrypted entries back to file
                entry.setEntries(decryptedEntries)
                # set the encrypted status to False
                entry.setEncrypted(False)

                usage = setUsage()
                password = setPassword(setPasswordLength())

                # append a new entry
                entry.createEntry(usage,password)
                # get the whole entry data
                entries = entry.getEntries()
                # encrypt the data
                encryptedEntries = encrypt.encrypt(entries)
                # write the encrypted data back to file
                entry.setEntries(encryptedEntries)
                # set encrypted status to True
                entry.setEncrypted(True)
            else:
                print("Entries are not encrypted.")
                print("Process canceled.")
                print("Address this issue immediately")
        elif option == 2:
            if config.getFirstRun():
                print("No entries have been set")
            if entry.getEncrypted() and not config.getFirstRun():
                encryptedEntries = entry.getEntries()
                decryptedEntries = encrypt.decrypt(encryptedEntries)
                print(decryptedEntries)
            else:
                print("Entries are not encrypted.")
                print("Process canceled.")
                print("Address this issue immediately")
        elif option == 3:
            print("Exiting password manager")
            exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()