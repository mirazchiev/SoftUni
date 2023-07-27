user_input = input()
result = ""
last = ""

for char in user_input:
    if last != char:
        result += char
    last = char
print(result)
# user_input = input()
#
# list_of_chars = []
# for char in user_input:
#     list_of_chars.append(char)
#
# for index in range(len(list_of_chars)-1):
#     if list_of_chars[index] == list_of_chars[index+1]:
#         list_of_chars[index] = "delete"
# print("".join(list_of_chars).replace("delete", ""))
