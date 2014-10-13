import json
import os
import operator
import protocolObjects
import md

protocolDescription = open("../protocolDescription/protocol.json", "r")
index = open("../index.md", "w")

types = json.load(protocolDescription)["types"]

def shouldExclude(item, items):
    prefix = "chromium_"
    itemName = item["typeName"]
    if itemName.startswith(prefix):
        for otherItem in items:
            if otherItem["typeName"] == itemName[len(prefix):]:
                return True
    return False

def cleanNames(itemList):
    prefix = "chromium_"
    for item in itemList:
        if item["typeName"].startswith(prefix):
            item["typeName"] = item["typeName"][len(prefix):]

def getList(completeList, category):
    categoryList = [types[objectType] for objectType in types if types[objectType]["category"] == category]
    noDuplicatesList = [entry for entry in categoryList if not shouldExclude(entry, categoryList)]
    cleanNames(noDuplicatesList)
    noDuplicatesList.sort(key=operator.itemgetter('typeName'))
    return noDuplicatesList

actors = getList(types, "actor")
dicts = getList(types, "dict")

index.write("\n## Actors ##\n\n")
for actor in actors:
    md.writeMDLink(actor["typeName"], actor["typeName"], index)
    md.writeLineBreak(index)
    protocolObjects.writeActor(actor, dicts)

index.write("\n## Dictionaries ##\n\n")
for dictionary in dicts:
    md.writeMDLink(dictionary["typeName"], dictionary["typeName"], index)
    md.writeLineBreak(index)

