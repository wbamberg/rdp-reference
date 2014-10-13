import json
import os
import operator
import md

def writeMessages(messages, actorName, output, dicts):
    md.writeH2("Messages", output)
    for message in messages:
        md.writeH3(message["name"], output)

        md.writeH4("Request", output)
        md.writeTableStart(output)
        md.writeTableRow(["to", actorName], output)
        md.writeTableRow(["type", message["request"]["type"]], output)
        for param in message["request"]:
            if param != "type":
                md.writeTableRow([param, message["request"][param]["type"]], output)
        md.writeTableEnd(output)

        retval = message["response"].get("_retval")
        if retval:
            dictionary = dicts.get(retval)
            print actorName + " : " + message["request"]["type"]
        else:
            responseList = message["response"].items()
            if len(responseList) > 0:
                md.writeH4("Response", output)
                output.write(responseList[0][1]["_retval"] + "\n")

def writeActor(actor, dicts):
    actorName = actor["typeName"]
    output = open("../docs/" + actorName + ".md", "w")
    md.writeH1(actorName, output)
    writeMessages(actor["methods"], actorName, output, dicts)
