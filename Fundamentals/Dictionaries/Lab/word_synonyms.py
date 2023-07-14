number_of_words = int(input())

synonyms = {}

for i in range(number_of_words):
    word = input()
    synonym = input()
    if word in synonyms:
        synonyms[word].append(synonym)
    else:
        synonyms[word] = [synonym]

for word, synonym in synonyms.items():
    print(f"{word} - {', '.join(synonym)}")

