def absoluteValuesSumMinimization(a):
    values = []
    for first in a:
        value = 0
        for second in a:
            value += abs(first - second)
        values.append((first, value))
    return sorted(values, key=lambda value: value[1])[0][0]
