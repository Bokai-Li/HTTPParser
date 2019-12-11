import sys
import re
from os import path

#regular expression for file path
absoluteFilePath = re.compile('^/[\w./]*$')
#regular expression for HTTP version
httpVersion = re.compile('^HTTP/\d[.]\d$')

#read input
userInput = sys.stdin.read()
processedInput = userInput.splitlines()
validInput = False
print(processedInput)
for item in processedInput:
    #check input to see if it is valid
    sys.stdout.write(item)
    sys.stdout.write("\r\n")
    item = re.sub(" +", " ", item)
    ParsedInput = item.split(" ")
    if ParsedInput[0] != 'GET':
        print("ERROR -- Invalid Method token.")
    elif len(ParsedInput) < 2 or (not absoluteFilePath.match(ParsedInput[1])):
        print("ERROR -- Invalid Absolute-Path token.")
    elif len(ParsedInput) < 3 or (not httpVersion.match(ParsedInput[2])):
        print("ERROR -- Invalid HTTP-Version token.")
    elif len(ParsedInput) > 3 and not(len(ParsedInput)==4 and ParsedInput[3]==""):
        print( "ERROR -- Spurious token before CRLF.")
    else:
        print("Method =",ParsedInput[0])
        print("Request-URL =",ParsedInput[1])
        print("HTTP-Version =", ParsedInput[2])
        validInput = True

        #process input if it is valid
    if validInput:
        #parse file extension
        localDirectoryPath = ParsedInput[1][1:]
        splitPathForExtension = ParsedInput[1].split(".")
        extension = splitPathForExtension[len(splitPathForExtension) - 1]
        extension = extension.lower()
        if not (extension == "txt" or extension == "htm" or extension == "html"):
            print("501 Not Implemented:",ParsedInput[1])
        elif not path.exists(localDirectoryPath):
            print("404 Not Found:",ParsedInput[1]) 
        else:
            f = open(localDirectoryPath, "r")
            try:
                data = f.read()
            except IOError as error:
                print("ERROR:",str(error))
            sys.stdout.write(data)
            f.close()



