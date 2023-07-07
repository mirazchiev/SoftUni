list_of_words = input().split()
even_words = [word for word in list_of_words if len(word) % 2 == 0]
for word in even_words:
    print(word)
