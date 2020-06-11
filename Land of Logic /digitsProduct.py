def digitsProduct(p):
    if p == 0: 
        return 10
    for i in range(3600):
        a = 1
        for j in str(i):
            a *= int(j)
        if a == p: 
            return i
    return -1


print(digitsProduct(12))  # => 26
print(digitsProduct(19))  # => -1
print(digitsProduct(450)) # => 2559