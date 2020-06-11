def deleteDigit(n):
    n = str(n)
    return max([int(n[:index] + n[index + 1:]) for index in range(len(n))])

print(deleteDigit(152))