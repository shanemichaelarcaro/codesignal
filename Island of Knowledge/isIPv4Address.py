# def isIPv4Address(inputString):
#     return len([num for num in inputString.split(".") if num != "" and 0 <= int(num) < 255]) == 4

# def isIPv4Address(inputString):
#     return len([int(num) for num in inputString.split(".") if num != "" and not num.islower() and 0 <= int(num) <= 255]) == 4

# def isIPv4Address(inputString):
#     print([num.isdigit() for num in inputString.split(".")])
#     print(inputString.count("."))
#     numbers = [int(num) for num in inputString.split(".") if num != "" and not num.islower() and 0 <= int(num) <= 255 and len(num) == len(str(int(num)))]
#     print(numbers)
#     print(len(numbers))
#     return len(numbers) == 4

def isIPv4Address(inputString):
    if inputString.count(".") != 3:
        return False
    return len([int(num) for num in inputString.split(".") if num != "" and not num.islower() and 0 <= int(num) <= 255 and len(num) == len(str(int(num)))]) == 4

#   172.16.254.1 => True
#   172.316.254.1 => False
#   .254.255.0 => False

print(isIPv4Address("0..1.0.0"))