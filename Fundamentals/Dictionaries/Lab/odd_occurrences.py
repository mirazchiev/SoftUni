words = input().split()

words_dictionary = {}

for word in words:
    word = word.lower()
    if word in words_dictionary:
        words_dictionary[word] += 1
    else:
        words_dictionary[word] = 1

keys = ""

for key, value in words_dictionary.items():
    if value % 2 != 0:
        keys += " " + key

print(keys[1:])
