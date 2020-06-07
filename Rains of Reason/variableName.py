def variableName(name):
    acceptable = [*range(48, 58), *range(65, 91), 95, *range(97, 123)]
    if 48 <= ord(name[0]) < 57 or ord(name[0]) not in acceptable:
        return False
    return all([ord(letter) in acceptable for letter in name])