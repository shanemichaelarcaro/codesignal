def isMAC48Address(inputString):
    string = inputString.lower().split("-")
    if len(string) != 6:
        return False
    for pair in string:
        if len(pair) != 2:
            return False
        for letter in pair:
            if not (97 <= ord(letter) <= 102 or 48 <= ord(letter) <= 57):
                return False
    return True


print(isMAC48Address("00-1B-63-84-45-E6"))  # => True
print(isMAC48Address("Z1-1B-63-84-45-E6"))  # => False
print(isMAC48Address("not a MAC-48 address"))  # => False
print(isMAC48Address("FF-FF-FF-FF-FF-FF"))  # => True
