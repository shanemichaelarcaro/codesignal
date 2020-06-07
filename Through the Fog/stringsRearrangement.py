def stringsRearrangement(inputArray):
    words = []
    for word in inputArray:
        total_value = 0
        for letter in word:
            total_value += ord(letter)
        words.append((total_value, word))
    words.sort(key=lambda value: value[0])
    print(words)

    for index in range(len(words) - 1):
        errors = 0
        for letter in range(len(words[index][1])):
            if words[index][1][letter] != words[index + 1][1][letter]:
                errors += 1
        if errors != 1:
                return False
    return True

    # print(words)


#   ['ab', 'bb', 'aa'] => True
#   ['aba', 'bbb', 'bab] => False

print(stringsRearrangement(['ab', 'bb', 'aa']))
print(stringsRearrangement(['aba', 'bbb', 'bab']))
print(stringsRearrangement(['ff', 'gf', 'af', 'ar', 'hf']))