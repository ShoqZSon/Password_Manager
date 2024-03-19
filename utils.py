import json

class Utils:
    @staticmethod
    def writeJson(path,data):
        with open(path,"w") as file:
            json.dump(data,file,indent=4)

    @staticmethod
    def readJson(path):
        with open(path,"r") as file:
            data = json.load(file)
            return data

    @staticmethod
    def writeBinary(path,data):
        with open(path, 'wb') as file:
            file.write(data)

    @staticmethod
    def readBinary(path):
        with open(path, 'rb') as file:
            data = file.read()
            return data

    @staticmethod
    def updateValJson(path,keyword,newVal):
        data = Utils.readJson(path)
        data[keyword] = newVal
        Utils.writeJson(path,data)

    @staticmethod
    def getValJson(path,keyword):
        data = Utils.readJson(path)

        if data[keyword]:
            return data[keyword]

    @staticmethod
    def question(placeholder):
        while True:
            answer = str(input(f"Choose '{placeholder}'? "))
            if answer == "y":
                return True
            elif answer == "n":
                return False
            else:
                print("Invalid answer. Try again.")

    @staticmethod
    def listToString(myList):
        resultString = '[' + ','.join([f'{x}' for x in myList]) + ']'
        return resultString

    @staticmethod
    def bytesToString(byteData):
        if isinstance(byteData, bytes):
            return byteData.decode('utf-8')  # Assuming utf-8 encoding
        else:
            raise ValueError("Input must be bytes type")

    @staticmethod
    def stringToBytes(stringData):
        if isinstance(stringData, str):
            return stringData.encode('utf-8')  # Assuming utf-8 encoding
        else:
            raise ValueError("Input must be string type")

    @staticmethod
    def stringToList(string):
        jsonAcceptableString = string.replace("'","\"")
        jsonString = json.loads(jsonAcceptableString)

        return jsonString

