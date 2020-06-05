def avoidObstacles(inputArray):
    jump = 2
    while True:
        if all(num % jump != 0 for num in inputArray):
            return jump
        jump += 1


#   [5, 3, 6, 7, 9]     => 4
#   [2, 3]              => 4
#   [1, 4, 10, 6, 2]    => 7
#   [1000, 999]         => 6
#   [19, 32, 11, 23]    => 3

avoidObstacles([5, 3, 6, 7, 9])