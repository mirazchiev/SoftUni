string = input()
result = ""
length = 0

for index in range(len(string)):
    if string[index] == ">":
        length += int(string[index+1])
        result += string[index]
        continue
    if length == 0:
        result += string[index]
    else:
        length -= 1

print(result)
