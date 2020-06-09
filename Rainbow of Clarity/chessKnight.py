def chessKnight(cell):
    positions, count = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1 , -2), (-2, -1), (-2, 1)], 0

    for position in positions:
        if 97 <= ord(cell[0]) + position[0] <= 104 and 1 <= int(cell[1]) + position[1] <= 8:
            count += 1
    return count
    
print(chessKnight("b7")) # => 2