strings = input().split()
message = ""
for string in strings:
    message += string * len(string)

print(message)
