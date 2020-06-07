def isBeautifulString(inputString):
    letters = list(sorted(set(inputString), reverse=True))
    return all(chr(number) in letters for number in range(ord(letters[0]), 96, - 1)) and \
     all(inputString.count(letters[index]) <= inputString.count(letters[index + 1]) for index in range(len(letters) - 1))

print(isBeautifulString("bbbaacdafe"))                  # => True
print(isBeautifulString("aabbb"))                       # => False
print(isBeautifulString("abcdefghijklmnopqrstuvwxyzz")) # => False
print(isBeautifulString("bbc"))                         # => False
