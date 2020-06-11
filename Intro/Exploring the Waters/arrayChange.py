def arrayChange(inputArray):
    total = 0
    for index in range(1, len(inputArray)):
        if inputArray[index] <= inputArray[index - 1]:
            value = abs(inputArray[index] - inputArray[index - 1]) + 1
            inputArray[index] += value
            total += value
    return total