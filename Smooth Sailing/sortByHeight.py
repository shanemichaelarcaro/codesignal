def sortByHeight(a):
    copy = a[:]
    while -1 in copy:
        copy.remove(-1)
    copy.sort()
    
    counter = 0
    for number in range(len(a)):
        if a[number] != -1:
            a[number] = copy[counter]
            counter += 1
    return a