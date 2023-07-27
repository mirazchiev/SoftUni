user_input = input()
result = ""
for char in user_input:
    # result += chr(ord(char) + 3)

    char_ascii_number = ord(char) + 3
    char = chr(char_ascii_number)
    result += char

print(result)
