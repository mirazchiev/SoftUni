user_input = input()
string = ""
number = ""
output = ""
unique_values = []
for index, char in enumerate(user_input):
    if char.isnumeric():
        number += char
        if index < len(user_input) - 1 and user_input[index+1].isnumeric():
            continue
        else:
            number = int(number)
            output += string * number
            string = ""
            number = ""

    else:
        string += char.upper()
        if char.upper() not in unique_values:
            unique_values.append(char.upper())

print(f"Unique symbols used: {len(unique_values)}")
print(output)
