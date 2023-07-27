def letter_operations(strings: list) -> float:
    total = 0
    for string in strings:
        string = string.strip()
        first_letter = string[0]
        last_letter = string[-1]
        number = int(string[1:-1])

        if first_letter == first_letter.upper():
            first_letter_position = ord(first_letter) - 64
            number /= first_letter_position
        elif first_letter == first_letter.lower():
            first_letter_position = ord(first_letter) - 96
            number *= first_letter_position

        if last_letter == last_letter.upper():
            last_letter_position = ord(last_letter) - 64
            number -= last_letter_position
        elif last_letter == last_letter.lower():
            last_letter_position = ord(last_letter) - 96
            number += last_letter_position

        total += number

    return total


user_input = input().split()
result = letter_operations(user_input)
print(f"{result:.2f}")
