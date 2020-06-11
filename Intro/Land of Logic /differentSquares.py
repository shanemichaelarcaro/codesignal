def differentSquares(matrix):
    numbers = []
    for col in range(len(matrix) - 1):
        for row in range(len(matrix[0]) - 1):
            number = matrix[col][row: row + 2] + matrix[col + 1][row: row + 2]
            if not number in numbers:
                numbers.append(number)
    return len(numbers)

matrix = [
    [1, 2, 1],
    [2, 2, 2],
    [2, 2, 2],
    [1, 2, 3],
    [2, 2, 1]
]
print(differentSquares(matrix)) # => 6