def alternatingSums(a):
    sumA = 0
    sumB = 0
    for index, weight in enumerate(a):
        if index % 2 == 0:
            sumA += weight
        else:
            sumB += weight
    return sumA, sumB