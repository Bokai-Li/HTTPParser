import os                                                                                     
import io
import sys
import string

def isDigitValid(digit):
    if digit not in string.digits:
        print("this digit is not in string.digit")
        return False
    return True

def isValidPathCharacter(character):
    # check upper case, lower case, digit, "." "_" "/"
    if not (character in string.ascii_uppercase or character in string.ascii_lowercase or character in string.digits or character == "." or character == "_" or character == "/"):
        return False
    return True



for line in sys.stdin:
    sys.stdout.write(line)
    inputStrings = line.split()
    #print(inputStrings)

    # check white space before GET
    if not line.startswith("GET"):
        print("ERROR -- Invalid Method token.")
        continue

    # check the GET method                                                                                                                                                                                       
    if len(inputStrings) < 1 or inputStrings[0] != "GET":
        print("ERROR -- Invalid Method token.")
        continue

    # check the relative path
    if len(inputStrings) < 2:
        print("ERROR -- Invalid Absolute-Path token.")
        continue
    absolutePath = inputStrings[1]
    isPathValid = True                                                                                                                                                                               
    if absolutePath[0] != "/":
        isPathValid = False
    if isPathValid:
        for character in absolutePath:
            if not isValidPathCharacter(character):
                isPathValid = False
                break
    if isPathValid == False:
        print("ERROR -- Invalid Absolute-Path token.")
        continue

    # check the http version
    if len(inputStrings) < 3:
        print("ERROR -- Invalid HTTP-Version token.")
        continue                                                                                                                                                                       
    httpVersion = inputStrings[2].split("/")
    
    # when there's less than 2 elt in the http version
    if len(httpVersion) < 2:
        print("ERROR -- Invalid HTTP-Version token.")
        continue 
    #print(httpVersion)
    versionIsValid = True
    if len(httpVersion) != 2:
        versionIsValid = False
    if versionIsValid and httpVersion[0] != "HTTP":
        versionIsValid = False
    digits = httpVersion[1].split(".")
    #print(digits)
    #rint(digits[1][0])
    if versionIsValid and len(digits) != 2:
        versionIsValid = False
    #print(digits[1])
    #print(digits[1].isdigit())
    if versionIsValid and ((digits[0].isdigit() == False) or (digits[1].isdigit() == False)):
        versionIsValid = False
    if versionIsValid == False:
        print("ERROR -- Invalid HTTP-Version token.")
        continue
    # spurious token before crlf error
    #digitsRemained = digits[1][1:]
    #print(digitsRemained)
    if len(inputStrings) > 3:
        print("ERROR -- Spurious token before CRLF.")
        continue
    # parse correct, print the component
    print("Method = GET")
    print("Request-URL = " + inputStrings[1])
    print("HTTP-Version = " + inputStrings[2])

    # 501 not implemented error                                                                                                                                                                     
    path = inputStrings[1].split(".")
    extention = path[len(path) - 1]
    extention = extention.lower()
    if extention != "txt" and extention != "htm" and extention != "html":
        print("501 Not Implemented: " + inputStrings[1])
        continue
    try:
        currentDirectory = os.getcwd()
        file = open(currentDirectory + inputStrings[1])
        try:
            data = file.read()
        except IOError as error:
            print("ERROR: " + str(error))
        sys.stdout.write(data)
        file.close()
    except IOError:
        print("404 Not Found: " + inputStrings[1])

