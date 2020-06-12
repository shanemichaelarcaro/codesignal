def circleOfNumbers(n, firstNumber):
    return firstNumber + (n + 1) // 2 if firstNumber < n / 2 else firstNumber - (n + 1) // 2