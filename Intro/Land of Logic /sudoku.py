def sudoku(grid):
    check = [row for row in grid]
    correct = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for col in range(len(grid)):
        column = []
        for row in range(len(grid[col])):
            column.append(grid[row][col])
        check.append(column)

    for col in range(0, len(grid), 3):
        for row in range(0, len(grid[col]), 3):
            column = []
            for height in range(col, col + 3):
                for width in range(row, row + 3):
                    column.append(grid[height][width])
            check.append(column)
            
    return all([sorted(index) == correct for index in check])

grid = [[1,2,3,4,5,6,7,8,9], 
 [1,2,3,4,5,6,7,8,9], 
 [1,2,3,4,5,6,7,8,9], 
 [1,2,3,4,5,6,7,8,9], 
 [1,2,3,4,5,6,7,8,9], 
 [1,2,3,4,5,6,7,8,9], 
 [1,2,3,4,5,6,7,8,9], 
 [1,2,3,4,5,6,7,8,9], 
 [1,2,3,4,5,6,7,8,9]]

print(sudoku(grid))