def messaging(numbers: list, string: str):
    index = 0
    list_of_letters = []
    for number in numbers:
        index = 0
        for digit in number:
            index += int(digit)
        while index + 1 > len(string):
            index -= len(string)
        list_of_letters.append(string[index])
        string = string[:index] + string[index + 1:]

    return "".join(list_of_letters)


list_of_numbers = input().split()
user_input = input()
result = messaging(list_of_numbers, user_input)
print(result)
