def knapsackLight(value1, weight1, value2, weight2, maxW):
    # weights = sorted([(value1, weight1), (value2, weight2)], key=lambda weight: weight[1])
    # print(weights)
    if weight1 > maxW and weight2 > maxW:
        return 0
    elif weight2 > maxW:
        return value1
    elif weight1 + weight2 > maxW:
        return max(value1, value2)
    else:
        return value1 + value2


print(knapsackLight(10, 5, 6, 4, 8)) # => 10
print(knapsackLight(10, 5, 6, 4, 9)) # => 16
print(knapsackLight(5, 3, 7, 4, 6)) # => 7

