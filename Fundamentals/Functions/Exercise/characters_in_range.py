def characters(char1, char2):
    ascii_characters_list = []
    ascii_value_1 = ord(char1)
    ascii_value_2 = ord(char2)
    for character in range(ascii_value_1 + 1, ascii_value_2):
        ascii_characters_list.append(chr(character))
    return " ".join(ascii_characters_list)


character1 = input()
character2 = input()
print(characters(character1, character2))
