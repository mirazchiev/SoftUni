def palindromes(list_of_words: list, palindrome: str):
    list_of_palindromes = []
    for word in list_of_words:
        word = str(word).lower()
        if word == word[::-1]:
            list_of_palindromes.append(word)
    return f'{list_of_palindromes}\nFound palindrome {list_of_palindromes.count(palindrome)} times'


user_input_list = input().split()
user_input_palindrome = input()
result = palindromes(user_input_list, user_input_palindrome)
print(result)
