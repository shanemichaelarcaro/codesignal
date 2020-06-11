def sumUpNumbers(inputString):
    numbers, number = [], ""
    for letter in inputString:
        if letter.isdigit():
            number += letter
        else:
            if number != "":
                numbers.append(int(number))
                number = ""
    if number != "":
        numbers.append(int(number))
    return sum(numbers)


print(sumUpNumbers("2 apples, 12 oranges"))                                     # => 14
print(sumUpNumbers("123450"))                                                   # => 123450
print(sumUpNumbers("there are some (12) digits 5566 in this 770 string 239"))   # => 6587
        

