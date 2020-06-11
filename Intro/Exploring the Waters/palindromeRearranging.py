def palindromeRearranging(inputString):
    characters = {}
    error_count = 0
    for character in inputString:
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    print(characters.values())
    for value in characters.values():
        print(value % 2)
        if value % 2 != 0:
            error_count += 1
    return error_count <= 1

print(palindromeRearranging("aaabb"))