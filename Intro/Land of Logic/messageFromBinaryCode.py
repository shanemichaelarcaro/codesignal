def messageFromBinaryCode(code):
    return "".join([chr(int(code[index: index + 8], 2)) for index in range(0, len(code), 8)])

print(messageFromBinaryCode("010010000110010101101100011011000110111100100001"))    # => Hello!