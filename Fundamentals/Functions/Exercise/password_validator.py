def password_validation(password):
    length_is_valid = False
    if 6 <= len(password) <= 10:
        length_is_valid = True
    else:
        print("Password must be between 6 and 10 characters")
    structure_is_valid = False
    if password.isalnum():
        structure_is_valid = True
    else:
        print("Password must consist only of letters and digits")
    strength_is_valid = False
    number_of_digits = 0
    for character in password:
        if character.isnumeric():
            number_of_digits += 1
    if number_of_digits >= 2:
        strength_is_valid = True
    else:
        print("Password must have at least 2 digits")
    return length_is_valid, structure_is_valid, strength_is_valid


user_password = input()
length, structure, strength = password_validation(user_password)
if length and structure and strength:
    print("Password is valid")
