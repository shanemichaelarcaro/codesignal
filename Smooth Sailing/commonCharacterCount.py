def commonCharacterCount(s1, s2):
    char_count = 0
    for index in range(len(s1)):
        if s1[index] in s2:
            char_count += 1
            found = s2.find(s1[index])
            s2 = s2[:found] + s2[found + 1:]
    return char_count