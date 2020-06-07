def bishopAndPawn(bishop, pawn):
    b_location = ord(bishop[0]) + int(bishop[1])
    p_location = ord(pawn[0]) + int(pawn[1])
    return ord(bishop[0]) != ord(pawn[0]) and b_location % 2 == p_location % 2


print(bishopAndPawn("a1", "c3")) # => True
print(bishopAndPawn("h1", "h3")) # => False
