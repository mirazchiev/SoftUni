def perfect_number(number):
    aliquot_sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            aliquot_sum += divisor
    if number == aliquot_sum:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


user_input = int(input())
result = perfect_number(user_input)
print(result)
