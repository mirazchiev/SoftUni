import re

sentence = input()
word = input()
pattern = fr"\b{word}\b"

number_of_matches = len(re.findall(pattern, sentence, re.IGNORECASE))
print(number_of_matches)
