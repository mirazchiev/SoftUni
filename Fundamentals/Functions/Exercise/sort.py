numbers = list(input().split(" "))
numbers_as_digits = []
for number in numbers:
    number_as_digit = int(number)
    numbers_as_digits.append(number_as_digit)
sorted_numbers = sorted(numbers_as_digits)
print(sorted_numbers)
