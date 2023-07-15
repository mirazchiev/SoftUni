string = input()

output_dict = {}

for i in range(len(string)):
    if string[i] == " ":
        continue
    if string[i] in output_dict:
        output_dict[string[i]] += 1
    else:
        output_dict[string[i]] = 1

for letter in output_dict:
    print(f"{letter} -> {output_dict[letter]}")
