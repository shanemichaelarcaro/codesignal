def digitDegree(n):
    changes = 0
    while n >= 10:
        changes += 1
        n = sum([int(x) for x in str(n)])
    return changes

print(digitDegree(5)) # => 0
print(digitDegree(100)) # => 1
print(digitDegree(91)) # => 2