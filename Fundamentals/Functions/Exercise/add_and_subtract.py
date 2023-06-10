def sum_numbers(num1, num2):
    result = num1 + num2
    return result


def subtract(result1, num3):
    result2 = result1 - num3
    print(result2)


def add_and_subtract(number1, number2, number3):
    subtract(sum_numbers(number1, number2), number3)


add_and_subtract(int(input()), int(input()), int(input()))
