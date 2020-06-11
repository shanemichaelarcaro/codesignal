def longestDigitsPrefix(inputString):
    numbers = []
    for number in inputString:
        if number.isdigit():
            numbers.append(number)
        else:
            break
    return "".join(numbers)


