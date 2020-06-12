def lateRide(n):
    return sum([int(number) for number in str(n // 60) + str(n % 60)])

print(lateRide(808)) #=> time = 13:28 = 14