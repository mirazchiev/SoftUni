# def vowel_remover(string: str):
#     new_string = ""
#     vowels = ['a', 'o', 'u', 'e', 'i']
#     for index, letter in enumerate(string):
#         letter = str(letter).lower()
#         if letter not in vowels:
#             new_string += letter
#     return new_string
#
#
# user_input = input()
# result = vowel_remover(user_input)
# print(result)

string = input()
new_string = ""
result = [letter for letter in string if letter.lower() not in ['a', 'o', 'u', 'e', 'i']]
print("".join(result))
