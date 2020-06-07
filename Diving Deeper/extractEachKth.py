def extractEachKth(inputArray, k):
    return [value for index, value in enumerate(inputArray) if index % k != k - 1]

