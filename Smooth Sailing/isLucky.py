def isLucky(n):
    lucky_number = list(str(n))
    length = len(lucky_number)
    first = lucky_number[:length // 2]
    second = lucky_number[length // 2:]
    return add(first) == add(second)

def add(number):
    total = 0
    for digit in number:
        total += int(digit)
    return total