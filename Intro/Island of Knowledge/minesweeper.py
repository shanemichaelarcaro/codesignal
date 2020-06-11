def minesweeper(matrix):

    r = []
    
    for i in range(len(matrix)):
        r.append([])
        for j in range(len(matrix[0])):
            l = -matrix[i][j]
            for x in [-1,0,1]:
                for y in [-1,0,1]:
                    if 0<=i+x<len(matrix) and 0<=j+y<len(matrix[0]):
                        l += matrix[i+x][j+y]

            r[i].append(l)
    return r


#   matrix = [
#   [true, false, false],
#   [false, true, false],
#   [false, false, false]
# ] =>
#   output = [
#   [1, 2, 1],
#   [2, 1, 1],
#   [1, 1, 1]
# ]

matrix = [
    [True, False, False],
    [False, True, False],
    [False, False, False]
]

minesweeper(matrix)