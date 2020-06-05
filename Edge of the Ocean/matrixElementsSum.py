def matrixElementsSum(matrix):
    total = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if row + 1 < len(matrix) and matrix[row][col] == 0:
                matrix[row + 1][col] = 0
            else:
                total += matrix[row][col]
    return total