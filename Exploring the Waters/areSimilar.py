def areSimilar(a, b):
    similar_index = 0
    for number in range(len(a)):
        if a[number] != b[number]:
            similar_index += 1
    equal = True

    a.sort()
    b.sort()
    for number in range(len(a)):
        if a[number] != b[number]:
            equal = False
            break
    return similar_index <= 2 and equal