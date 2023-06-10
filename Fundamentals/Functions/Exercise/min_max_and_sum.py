def minimum(numbers):
    min_value = numbers[0]
    for min_number in numbers[1:]:
        if min_number < min_value:
            min_value = min_number
    return min_value


def maximum(numbers):
    max_value = numbers[0]
    for max_number in numbers[1:]:
        if max_number > max_value:
            max_value = max_number
    return max_value


def summed(numbers):
    summed_numbers = 0
    for sum_number in numbers:
        summed_numbers += sum_number
    return summed_numbers


list_of_numbers_as_strings = list(input().split())
list_of_numbers_as_integers = []
for number in list_of_numbers_as_strings:
    number_as_integer = int(number)
    list_of_numbers_as_integers.append(number_as_integer)
minimum_value = minimum(list_of_numbers_as_integers)
maximum_value = maximum(list_of_numbers_as_integers)
summed_value = summed(list_of_numbers_as_integers)
print(f"The minimum number is {minimum_value}")
print(f"The maximum number is {maximum_value}")
print(f"The sum number is: {summed_value}")
