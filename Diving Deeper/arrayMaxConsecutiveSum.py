# Solution works but execution times out with 1 out of 20 tests
# def arrayMaxConsecutiveSum(inputArray, k):
#     return max([sum(inputArray[index: index + k]) for index in range(len(inputArray) - (k - 1))])

def arrayMaxConsecutiveSum(inputArray, k):
    s = m = sum(inputArray[:k])
    for i in range(k, len(inputArray)):
        s += inputArray[i] - inputArray[i-k]
        if s > m: m = s
    return m

print(arrayMaxConsecutiveSum([2, 3, 5, 1, 6], 2)) # => 8
print(arrayMaxConsecutiveSum([2, 4, 10, 1], 2)) # => 14
print(arrayMaxConsecutiveSum([1, 3, 2, 4], 3)) # => 9