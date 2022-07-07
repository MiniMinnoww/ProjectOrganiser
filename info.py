# A place to get all the central info and objects
import json

settings = json.load(open("settings.json", "r"))

def GetSetting(jsonString):
    new = settings
    for line in jsonString.split("."):
        new = new[line]
    return new