list_of_numbers = list(map(int, input().split()))

while True:
    command = input()
    if command == "end":
        break
    elif "exchange" in command:
        command_index = command.split()
        index = int(command_index[1])
        if 0 <= index < len(list_of_numbers):
            list_of_numbers = list_of_numbers[index + 1:] + list_of_numbers[:index + 1]
        else:
            print("Invalid index")
    elif "max" in command:
        command_sub_command = command.split()
        sub_command = command_sub_command[1]
        if sub_command == "even":
            list_of_evens = [number for number in list_of_numbers if number % 2 == 0]
            if not list_of_evens:
                print("No matches")
            else:
                max_even = max(list_of_evens)
                print(max(index for index, value in enumerate(list_of_numbers) if value == max_even))
        elif sub_command == "odd":
            list_of_odds = [number for number in list_of_numbers if number % 2 != 0]
            if not list_of_odds:
                print("No matches")
            else:
                max_odd = max(list_of_odds)
                print(max(index for index, value in enumerate(list_of_numbers) if value == max_odd))
    elif "min" in command:
        command_sub_command = command.split()
        sub_command = command_sub_command[1]
        if sub_command == "even":
            list_of_evens = [number for number in list_of_numbers if number % 2 == 0]
            if not list_of_evens:
                print("No matches")
            else:
                min_even = min(list_of_evens)
                print(max(index for index, value in enumerate(list_of_numbers) if value == min_even))
        elif sub_command == "odd":
            list_of_odds = [number for number in list_of_numbers if number % 2 != 0]
            if not list_of_odds:
                print("No matches")
            else:
                min_odd = min(list_of_odds)
                print(max(index for index, value in enumerate(list_of_numbers) if value == min_odd))
    elif "first" in command:
        command_count_sub_command = command.split()
        count = int(command_count_sub_command[1])
        sub_command = command_count_sub_command[2]
        if count > len(list_of_numbers):
            print("Invalid count")
        else:
            result = []
            if sub_command == "even":
                list_of_evens = [number for number in list_of_numbers if number % 2 == 0]
                for i in range(min(count, len(list_of_evens))):
                    result.append(list_of_evens[i])
            elif sub_command == "odd":
                list_of_odds = [number for number in list_of_numbers if number % 2 != 0]
                for i in range(min(count, len(list_of_odds))):
                    result.append(list_of_odds[i])
            print(result)
    elif "last" in command:
        command_count_sub_command = command.split()
        count = int(command_count_sub_command[1])
        sub_command = command_count_sub_command[2]
        if count > len(list_of_numbers):
            print("Invalid count")
        else:
            result = []
            if sub_command == "even":
                list_of_evens = [number for number in list_of_numbers if number % 2 == 0][-count:]
                for i in range(min(count, len(list_of_evens))):
                    result.append(list_of_evens[i])
            elif sub_command == "odd":
                list_of_odds = [number for number in list_of_numbers if number % 2 != 0][-count:]
                for i in range(min(count, len(list_of_odds))):
                    result.append(list_of_odds[i])
            print(result)
print(list_of_numbers)
