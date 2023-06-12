def zeros(list_of_numbers: list):
    zeros_list = []
    non_zeros_list = []
    for number in list_of_numbers:
        number = int(number)
        if number == 0:
            zeros_list.append(number)
        else:
            non_zeros_list.append(number)
    return non_zeros_list + zeros_list


user_input = input().split(", ")
result = zeros(user_input)
print(result)
