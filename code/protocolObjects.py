import json
import os
import operator
import md

def cleanName(name):
    prefix = "chromium_"
    if name.startswith(prefix):
        return name[len(prefix):]
    return name

def getDictionary(typeName, dicts):
    for dictionary in dicts:
        if dictionary["typeName"] == typeName:
            return dictionary
    return None

def writeMessages(messages, actorName, output, dicts):
    md.writeH2("Messages", output)
    for message in messages:
        md.writeH3(message["name"], output)

        md.writeTableStart(output)
        md.writeTableRow(["to", actorName], output)
        md.writeTableRow(["type", message["request"]["type"]], output)
        for param in message["request"]:
            if param != "type":
                md.writeTableRow([param, message["request"][param]["type"]], output)
        md.writeTableEnd(output)

        retval = message["response"].get("_retval")
        # then it's specified at the top-level, and we should unpack it into
        # its component pieces
        if retval:
            md.writeH4("Response", output)
            retval = cleanName(retval)
            dictionary = getDictionary(retval, dicts)
            if dictionary != None:
                # then retval is defined as a dictionary type
                md.writeTableStart(output)
                md.writeTableRow(["from", actorName], output)
                for specialization in dictionary["specializations"]:
                    md.writeTableRow([specialization, dictionary["specializations"][specialization]], output)
                md.writeTableEnd(output)
            else:
                # the retval isn't really defined, and we just have to write what we have
                output.write(retval)
                md.writeLineBreak(output)
                print actorName + " : " + message["name"] + " : " + retval + " : is not a predefined dictionary"
        else:
            responseList = message["response"].items()
            if len(responseList) > 0:
                md.writeH4("Response", output)
                output.write(responseList[0][1]["_retval"] + "\n")

def writeActor(actor, dicts):
    actorName = actor["typeName"]
    output = md.createFile("../docs/" + actorName + ".md")
    md.writeH1(actorName, output)
    writeMessages(actor["methods"], actorName, output, dicts)
