# Password Manager
Password Manager written in Python 3

## Tools:
Python 3

## Important Libraries:
Cryptography, hashlib

## Functionality:
### First startup:
1. Config file will be created inside the folder where the .exe is located.
    - The config file contains the directories of:
        - its own directory
        - the password json file
        - the key
        - the hashed password
    - Also it holds a flag to retain whether the program is being executed for the first time or not.
2. The master password will be set and saved as a hash in the config
3. The key will be created and saved in folder where the .exe is located
4. An empty password json file will be created and also saved in the same folder where the .exe is located
### Non-first startup:
1. The master password has to be given in order to access the program
2. Three options will be given:
    - Create a new password
    - Show all passwords
    - Exit

## To-Do's
[x] Config creation \
[x] Setting Master Password and compare with user input \
[x] Creating the key for encryption \
[x] Encrypting the Entries array \
[x] Decrypting the Entries array \

## Security Measurements:
[ ] Error handling \
[ ] Securing the config file \
[ ] preventing unauthorized alteration of config file \
