def shapeArea(n):
    length = n * 2 - 1
    sumT = length
    for i in range(length - 2, 0, -2):
        sumT += i * 2
        print(i)
    return sumT