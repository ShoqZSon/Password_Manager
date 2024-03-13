import os
import json

from cryptography.fernet import Fernet
from utils import Utils

class Encryption:
    def __init__(self):
        config_data = Utils.readJson(os.path.join(os.getcwd(), "config.json"))
        key_path = config_data["KeyPath"]
        self.__key = Utils.readBinary(key_path)


