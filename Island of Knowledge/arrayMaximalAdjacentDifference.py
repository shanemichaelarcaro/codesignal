def arrayMaximalAdjacentDifference(inputArray):
    return max([abs(inputArray[x] - inputArray[x + 1]) for x in range(len(inputArray) - 1)])

# [2. 4, 1, 0] => 3
# [1, 1, 1, 1] => 1
# [-1, 4, 10, 3, -2] => 7
# [10, 11, 13] => 2

print(arrayMaximalAdjacentDifference([1, 1, 1, 1]))