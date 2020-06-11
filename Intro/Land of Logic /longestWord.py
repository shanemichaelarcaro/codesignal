def longestWord(text):
    return max("".join([letter if 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122 or \
        ord(letter) == 32 else " " for letter in text]).split(), key=len)

print(longestWord("Ready, steady, go!"))    # => steady