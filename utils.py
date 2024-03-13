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
            answer = str(input(f"Choose '{placeholder}'?"))
            if answer == "y":
                return True
            elif answer == "n":
                return False
            else:
                print("Invalid answer. Try again.")