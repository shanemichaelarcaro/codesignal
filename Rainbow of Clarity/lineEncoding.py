def lineEncoding(s):
    substrings = []
    for letter in s:
        if len(substrings) > 0 and letter in substrings[-1]:
            substrings[-1].append(letter)
        else:
            substrings.append(list(letter))
    return "".join([str(len(string)) + string[0] if len(string) > 1 else string[0] for string in substrings])

print(lineEncoding('aabbbc'))
