def chessBoardCellColor(cell1, cell2):
    w_diff = abs(ord(cell1[0]) - ord(cell2[0])) % 2
    h_diff = abs(int(cell1[1]) - int(cell2[1])) % 2

    if w_diff == 0:
        if h_diff == 0:
            return True
        else:
            return False
    else:
        if h_diff == 0:
            return False
    return True
