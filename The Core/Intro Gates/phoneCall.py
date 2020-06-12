def phoneCall(min1, min2_10, min11, s):
    minutes = 0
    if s - min1 < 0:
        return minutes
    minutes += 1
    s -= min1
    while s > 0:
        minutes += 1
        if 1 <= minutes <= 10:
            s -= min2_10
        elif minutes > 10:
            s -= min11
    if s < 0:
        minutes -= 1
    return minutes
    

print(phoneCall(10, 1, 2, 22)) # => 11