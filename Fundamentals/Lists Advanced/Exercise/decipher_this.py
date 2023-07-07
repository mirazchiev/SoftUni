def decipher_message(words: list):
    deciphered_words = []

    for word in words:
        char_code = ""
        counter = 0
        counter2 = 0
        for code in word:
            if code.isdigit():
                char_code += code
                counter += 1
            else:
                counter2 += 1
        first_letter = chr(int(char_code))
        second_letter = word[-1]
        if counter2 == 1:
            last_letter = ""
        else:
            last_letter = word[counter]
        middle_letters = word[counter + 1:- 1]
        deciphered_word = first_letter + second_letter + middle_letters + last_letter
        deciphered_words.append(deciphered_word)

    return ' '.join(deciphered_words)


user_input = input().split()
deciphered_message = decipher_message(user_input)
print(deciphered_message)
