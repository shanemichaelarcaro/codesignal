def evenDigitsOnly(n):
    for number in str(n):
        if int(number) % 2 != 0:
            return False
    return True