def growingPlant(upSpeed, downSpeed, desiredHeight):
    height = upSpeed
    difference = upSpeed - downSpeed
    day = 1

    while height < desiredHeight:
        # print(f"Day: {day}, Height: {height}")
        height += difference
        day += 1
    # print(f"Day: {day}, Height: {height}")
    return day



print(growingPlant(100, 10, 910)) # => 10
print(growingPlant(10, 9, 4)) # => 1
print(growingPlant(5, 2, 7)) # => 2