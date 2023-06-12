def exchange(user_command: str, list_of_numbers: list):
    exchange_index = int(user_command[9:])
    if len(list_of_numbers) - 1 < exchange_index < 0:
        print("Invalid index")
    else:
        list_of_numbers = list_of_numbers[exchange_index:] + list_of_numbers[:exchange_index]
    return list_of_numbers


def max_even_odd(user_command: str, list_of_numbers: list):
    max_list = []
    max_index = 0
    if "even" in user_command:
        for index, number in list_of_numbers:
            number = int(number)
            if number % 2 == 0:
                max_list.append(number)
                if number == max(max_list):
                    max_index = index

    elif "odd" in user_command:
        for index, number in list_of_numbers:
            number = int(number)
            if number % 2 != 0:
                max_list.append(number)
                if number == int(max(max_list)):
                    max_index = index
    return max_index


initial_list = list(map(int, input().split()))
command = ""
while command != "end":
    command = input()
    if "exchange" in command:
        result = exchange(command, initial_list)
        print(result)
    elif "max" in command:
        result = max_even_odd(command, initial_list)
        print(result)

