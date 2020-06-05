def makeArrayConsecutive2(statues):
    statues.sort()
    count = 0
    print(statues)
    for i in range(len(statues) - 1):
        if statues[i + 1] - 1 > statues[i]:
            count += statues[i + 1] - statues[i] - 1
    return count
