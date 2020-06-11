def adjacentElementsProduct(inputArray):
    pairs = []
    for i in range(len(inputArray) - 1):
        pairs.append(inputArray[i] * inputArray[i + 1])

    highestSum = pairs[0]
    for i in pairs:
        if i > highestSum:
            highestSum = i
    return highestSum