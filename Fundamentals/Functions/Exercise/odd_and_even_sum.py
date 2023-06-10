def odd_and_even(number):
    odd_sum = 0
    even_sum = 0
    for digit in number:
        digit = int(digit)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    result = f'Odd sum = {odd_sum}, Even sum = {even_sum}'
    return result


number = str(input())
print(odd_and_even(number))
