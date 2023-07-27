def char_multiplier(strings: list) -> int:
    first_word = strings[0]
    second_word = strings[1]
    total = 0
    if len(first_word) == len(second_word):
        for char_index in range(len(first_word)):
            total += ord(first_word[char_index]) * ord(second_word[char_index])
    else:
        if len(first_word) > len(second_word):
            longer = first_word
            shorter = second_word
        else:
            longer = second_word
            shorter = first_word
        for char_index in range(len(shorter)):
            total += ord(shorter[char_index]) * ord(longer[char_index])
        for char_index in range(len(shorter), len(longer)):
            total += ord(longer[char_index])

    return total


user_input = input().split()
result = char_multiplier(user_input)
print(result)
