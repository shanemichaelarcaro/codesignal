def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for index, value in enumerate(inputArray):
        if not elemToReplace in inputArray:
            break
        if value == elemToReplace:
            inputArray[index] = substitutionElem
    return inputArray