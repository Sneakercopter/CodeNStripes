import base64
import math
import string

def adidas_microchallenge_1(inp):
    # All the Ascii characters except for strings
    letters = list(string.printable[10:])
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    
    # Change all letters to their ascii values
    tmp = []
    for let in inp:
        if let in letters:
            tmp.append(int(ord(let)))
        else:
            tmp.append(int(let))
    inp = tmp
    
    # We will say this is a numerical problem
    # For now, we just return it b64 encoded
    if len(inp) == 1:
        # If the length is just the mode, then fine - just return it
        inp = str(inp[0])
        return base64.b64encode(inp.encode("utf-8")).decode("utf-8")
    # Haven't tested beyond length 2 yet but assume this
    elif len(inp) == 2:
        # We need to square the first number, and append the rest
        squaredMode = (int(inp[0]) ** 2)
        toEncode = str(squaredMode) + str(inp[len(inp) - 1])
        return base64.b64encode(toEncode.encode("utf-8")).decode("utf-8")
    # Here its the same as above, but we prepend the binary representation of the first
    # number
    elif len(inp) == 3:
        binaryPrefix = bin(int(inp[0]))[2:]
        squaredMode = (int(inp[1]) ** 2)
        toEncode = str(binaryPrefix) + str(squaredMode) + str(inp[len(inp) - 1])
        return base64.b64encode(toEncode.encode("utf-8")).decode("utf-8")
    elif len(inp) == 4:
        flooring = math.floor(int(inp[0]) / 2)
        binaryPrefix = bin(int(inp[1]))[2:]
        squaredMode = (int(inp[2]) ** 2)
        toEncode = str(flooring) + str(binaryPrefix) + str(squaredMode) + str(inp[len(inp) - 1])
        return base64.b64encode(toEncode.encode("utf-8")).decode("utf-8")
    # Here we need the octet representation of inp[0]
    elif len(inp) == 5:
        octet = oct(int(inp[0]))[2:]
        flooring = math.floor(int(inp[1]) / 2)
        binaryPrefix = bin(int(inp[2]))[2:]
        squaredMode = (int(inp[3]) ** 2)
        toEncode = str(octet) + str(flooring) + str(binaryPrefix) + str(squaredMode) + str(inp[len(inp) - 1])
        return base64.b64encode(toEncode.encode("utf-8")).decode("utf-8")
    # Here we add it to the alphabet
    elif len(inp) == 6:
        letterIndex = int(inp[0])
        if letterIndex > 25: 
            strRep = str(letterIndex)
            letterIndex = int(strRep[len(strRep) - 1])
        letter = alphabet[letterIndex]
        octet = oct(int(inp[1]))[2:]
        flooring = math.floor(int(inp[2]) / 2)
        binaryPrefix = bin(int(inp[3]))[2:]
        squaredMode = (int(inp[4]) ** 2)
        toEncode = str(letter) + str(octet) + str(flooring) + str(binaryPrefix) + str(squaredMode) + str(inp[len(inp) - 1])
        return base64.b64encode(toEncode.encode("utf-8")).decode("utf-8")