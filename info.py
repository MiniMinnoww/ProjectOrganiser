# A place to get all the central info and objects
import json

tiles = []

settings = json.load(open("json/settings.json", "r"))

def GetSetting(jsonString):
    new = settings
    for line in jsonString.split("."):
        new = new[line]
    return new