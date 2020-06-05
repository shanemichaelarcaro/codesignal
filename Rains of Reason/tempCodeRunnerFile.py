def chessBoardCellColor(cell1, cell2):
    return abs(ord(cell1[0]) - ord(cell2[0])) % 2 == 0

print(chessBoardCellColor('A1', 'C3'))