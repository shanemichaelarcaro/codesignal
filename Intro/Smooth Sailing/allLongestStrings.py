def allLongestStrings(inputArray):
    output = []
    max_length = 0
    for word in inputArray:
        if len(word) > max_length:
            max_length = len(word)

    for word in inputArray:
        if len(word) == max_length:
            output.append(word)
    return output
