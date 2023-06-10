def is_even(number):
    if number % 2 == 0:
        return True
    return False


numbers = list(map(int, (input().split())))
even_numbers = filter(is_even, numbers)
even_numbers_list = list(even_numbers)
print(even_numbers_list)
