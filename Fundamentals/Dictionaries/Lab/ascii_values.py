letters = input().split(", ")

dictionary = {}

for letter in letters:
    dictionary[letter] = ord(letter)

print(dictionary)
