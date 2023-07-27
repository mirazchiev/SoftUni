user_input = input()

for index in range(len(user_input)):
    if user_input[index] == ":":
        print(user_input[index] + user_input[index + 1])
