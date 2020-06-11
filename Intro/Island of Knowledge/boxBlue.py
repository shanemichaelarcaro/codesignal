def boxBlur(m):
    r = len(m)
    c = len(m[0])
    ans = []
    for i in range(1,r-1):
        row=[]
        for j in range(1,c-1):
            row.append(sum([m[i+k][j+l] for k in [-1,0,1] for l in [-1,0,1]])//9)
        ans.append(row)
    return ans


# [
#   [1, 1, 1],
#   [1, 7, 1],
#   [1, 1, 1]
# ] = [[1]]

# [
#   [7, 4, 0, 1],
#   [5, 6, 2, 2],
#   [6, 10, 7, 8],
#   [1, 4, 2, 0]
# ] = [[5, 4], [4, 4]

input1 = [
    [1, 1, 1],
    [1, 7, 1],
    [1, 1, 1]
]

input2 = [
    [7, 4, 0, 1],
    [5, 6, 2, 2],
    [6, 10, 7, 8],
    [1, 4, 2, 0]
]

input3 = [
    [36, 0, 18, 9],
    [27, 54, 9, 0],
    [81, 63, 72, 45]
]
print(boxBlur(input3))