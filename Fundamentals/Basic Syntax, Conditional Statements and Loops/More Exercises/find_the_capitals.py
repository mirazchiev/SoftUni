def find_the_capital(word: str):
    list_of_uppers = []
    for character in range(len(word)):
        if 64 < ord(word[character]) < 91:
            list_of_uppers.append(character)
    return list_of_uppers


user_input = input()
result = find_the_capital(user_input)
print(result)
