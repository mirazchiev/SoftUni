def decrypting(message):
    ascii_code = ord(message) + user_key
    output_message = chr(ascii_code)
    return output_message


user_key = int(input())
number_of_inputs = int(input())
output = []
for input_index in range(number_of_inputs):
    user_input = input()
    result = decrypting(user_input)
    output.append(result)
print("".join(output))
