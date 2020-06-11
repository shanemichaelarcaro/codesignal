def validTime(time):
    time = time.split(":")
    return 0 <= int(time[0]) <= 23 and 1 <= int(time[1]) <= 59



print(validTime("13:58"))   # => True
print(validTime("25:51"))   # => False
print(validTime("02:78"))   # => False


