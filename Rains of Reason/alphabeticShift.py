def alphabeticShift(inputString):
    outputString = ""
    for value in inputString:
        if ord(value) == 122:
            outputString += chr(97)
        else:
            outputString += chr(ord(value) + 1)
    return outputString

print(alphabeticShift('crazy'))
# print(oct(122))