def even_numbers(numbers: list):
    even_number_indexes = []
    for index, number in enumerate(numbers):
        if number % 2 == 0:
            even_number_indexes.append(index)
    return even_number_indexes


list_of_numbers = list(map(int, input().split(", ")))
result = even_numbers(list_of_numbers)
print(result)
