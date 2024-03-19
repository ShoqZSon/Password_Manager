from config import Config
from entry import Entry
from key import Key
from encryption import Encryption
from utils import Utils

import hashlib
import string
import random

# checks if there is a master password set inside the config file
def checkPassword(path,user_password):
    data = Utils.readJson(path)
    password = data["MasterPassword"]
    if password == user_password:
        return True
    else:
        return False

# sets the password that will be used for authorization at the start
def setMasterPassword():
    password = str(input("Please enter your initial master password: "))
    if Utils.question(password):
        return password
    else:
        setMasterPassword()

# hashes the master password
def hashPassword(password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed

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

# takes the password length, shuffles a-z,A-Z,0-9 and punctuation (except " and ')
def setPassword(length):
    punctuation = "!#$%&()*+,-./:;<=>?@[\]^_`{|}~"
    characters = string.ascii_letters + string.digits + punctuation
    random.shuffle(list(characters))

    passwordList = [""] * length
    while True:
        for _ in range(length):
            passwordList.append(random.choice(characters))

        password = "".join(passwordList)
        if Utils.question(password):
            return password
        else:
            setPassword(length)

# sets the use case for the password
def setUsage():
    while True:
        usage = str(input("Enter the passwords usage: "))
        if Utils.question(usage):
            break

    return usage

def main():
    print("---- Password Manager ----")
    config = Config()
    # checks if the config file exists
    # if it does it asks for the master password
    # else it creates:
        # the config with default values
        # master password, hashes it and saves it
        # creates the key for encryption of the entries
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

        # creation of the key object
        key = Key(configPath)
        # generate the key and return it
        key_k = key.generateKey()
        # sets the private attribute key in the key object
        key.setKey(key_k)
        # sets the private attribute keyPath in the key object
        key.setKeyPath(config.getKeyPath())
        # writes the actual key
        key.writeKey()

        # creates the entry object with the proper config path
        entry = Entry(configPath)

        # creates the initial file where the entries will be stored
        entry.createInitialEntryFile()

    encrypt = Encryption(configPath)

    while True:
        print("Options:")
        print("1. Generate a new entry")
        print("2. Show stored passwords")
        print("3. Exit")
        option = int(input("Enter your option: "))
        if option == 1:
            # if the firstRun flag is set on True no decryption needed
            # and appending to the empty list
            if config.getFirstRun():
                usage = setUsage()
                password = setPassword(setPasswordLength())

                entry.createEntry(usage,password)
                entries = entry.getEntries()

                entryString = Utils.listToString(entries)
                encryptedEntries = encrypt.encrypt(entryString)

                try:
                    encryptedEntries = Utils.bytesToString(encryptedEntries)
                except Exception as e:
                    print(e)

                entry.setEntries(encryptedEntries)
                entry.setEncrypted(True)
                config.setFirstRun(False)
            elif entry.getEncrypted() and not config.getFirstRun():
                # get the whole entry data
                encryptedEntriesString = entry.getEntries()

                # convert string to bytes
                encryptedEntryBytes = Utils.stringToBytes(encryptedEntriesString)

                # decrypt the data
                decryptedEntries = encrypt.decrypt(encryptedEntryBytes)
                jsonEntries = Utils.stringToList(decryptedEntries)

                # write the decrypted entries back to file
                entry.setEntries(jsonEntries)
                # set the encrypted status to False
                entry.setEncrypted(False)

                usage = setUsage()
                password = setPassword(setPasswordLength())

                # append a new entry
                entry.createEntry(usage,password)
                # get the whole entry data
                entries = entry.getEntries()

                entries = Utils.listToString(entries)

                # encrypt the data
                encryptedEntries = encrypt.encrypt(entries)
                encryptedEntriesString = Utils.bytesToString(encryptedEntries)
                # write the encrypted data back to file
                entry.setEntries(encryptedEntriesString)
                # set encrypted status to True
                entry.setEncrypted(True)
            else:
                print("Entries are not encrypted.")
                print("Process canceled.")
                print("Address this issue immediately")
        elif option == 2:
            if config.getFirstRun():
                print("No entries have been set")
            elif entry.getEncrypted() and not config.getFirstRun():
                encryptedEntries = entry.getEntries()
                decryptedEntries = encrypt.decrypt(encryptedEntries)
                entryList = Utils.stringToList(decryptedEntries)
                for entry in entryList:
                    for key, value in entry.items():
                        print(f'{key}: {value}')
                    print("")
            else:
                print("Entries are not encrypted.")
                print("Process canceled.")
                print("Address this issue immediately")
        elif option == 3:
            print("Closing password manager")
            exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()