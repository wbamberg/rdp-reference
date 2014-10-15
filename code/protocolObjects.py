import json
import os
import operator
import md

def formatType(unformatted):
    components = unformatted.split(":")
    formatted = ""
    for component in components:
        if component == "array":
            formatted = formatted + "Array of "
        elif component == "nullable":
            formatted = formatted + "Null or "
        else:
            formatted = formatted + cleanName(component)
    return formatted

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
    if messages:
        md.writeH2("Messages", output)
    for message in messages:
        md.writeH3(message["name"], output)

        md.writeTableStart(output)
        md.writeTableRow(["to", actorName], output)
        md.writeTableRow(["type", message["request"]["type"]], output)
        for param in message["request"]:
            if param != "type":
                md.writeTableRow([param, formatType(message["request"][param]["type"])], output)
        md.writeTableEnd(output)

        retval = message["response"].get("_retval")
        if retval:
            # then it's specified at the top-level, and we should unpack it into
            # its component pieces
            md.writeH4("Response", output)
            retval = cleanName(retval)
            dictionary = getDictionary(retval, dicts)
            if dictionary != None:
                # then retval is defined as a dictionary type
                md.writeTableStart(output)
                md.writeTableRow(["from", actorName], output)
                for specialization in dictionary["specializations"]:
                    md.writeTableRow([specialization, formatType(dictionary["specializations"][specialization])], output)
                md.writeTableEnd(output)
            else:
                # the retval isn't really defined, and we just have to write what we have
                output.write(retval)
                md.writeLineBreak(output)
                #print actorName + " : " + message["name"] + " : " + retval + " : is not a predefined dictionary"
        else:
            # then retval isn't specified at the top level, and we have to dig into "response"
            # items in response are either strings, in which case that's the value
            # or they are dictionaries containing a single key "_retval", whose value is the item value
            # ugh!
            if message["response"]:
                md.writeH4("Response", output)
                response = message["response"]
                md.writeTableStart(output)
                md.writeTableRow(["from", actorName], output)
                for responseItemName in response:
                    if isinstance(response[responseItemName], dict):
                        md.writeTableRow([responseItemName, formatType(response[responseItemName]["_retval"])], output)
                    else:
                        md.writeTableRow([responseItemName, formatType(response[responseItemName])], output)
                md.writeTableEnd(output)

def writeEvents(events, actorName, output, dicts):
    if events:
        md.writeH2("Events", output)
    for event in events:
        md.writeH3(event, output)

        md.writeTableStart(output)
        md.writeTableRow(["from", actorName], output)
        md.writeTableRow(["type", events[event]["type"]], output)
        for param in events[event]:
            if param != "type":
                if isinstance(events[event][param], dict):
                    md.writeTableRow([param, formatType(events[event][param]["type"])], output)
                else:
                    md.writeTableRow([param, formatType(str(events[event][param]))], output)
        md.writeTableEnd(output)


def writeActor(actor, dicts):
    actorName = actor["typeName"]
    output = md.createFile("../docs/" + actorName + ".md")
    md.writeH1(actorName, output)
    writeMessages(actor["methods"], actorName, output, dicts)
    writeEvents(actor["events"], actorName, output, dicts)

def writeProperties(properties, dictName, output, dicts):
    if not properties:
        return
    md.writeH2("Properties", output)
    md.writeTableStart(output)

    for prop in properties:
        md.writeTableRow([prop, formatType(properties[prop])], output)

    md.writeTableEnd(output)

def writeDict(dictionary, dicts):
    dictName = dictionary["typeName"]
    output = md.createFile("../docs/" + dictName + ".md")
    md.writeH1(dictName, output)
    writeProperties(dictionary["specializations"], dictName, output, dicts)
