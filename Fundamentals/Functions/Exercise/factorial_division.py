def factorial_division(number1, number2):
    first_factorial = 1
    for multiplier in range(1, number1 + 1):
        first_factorial *= multiplier
    second_factorial = 1
    for multiplier in range(1, number2 + 1):
        second_factorial *= multiplier
    result = first_factorial / second_factorial
    return result


first_input = int(input())
second_input = int(input())
print(f"{factorial_division(first_input, second_input):.2f}")
