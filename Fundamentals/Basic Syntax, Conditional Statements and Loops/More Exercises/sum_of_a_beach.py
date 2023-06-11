def beach_counter(string: str):
    counter = 0
    for index in range(len(string)):

        if (len(string) - index) >= 4:
            if string[index] == "s":
                if string[index + 1] == "a":
                    if string[index + 2] == "n":
                        if string[index + 3] == "d":
                            counter += 1

        if (len(string) - index) >= 5:
            if string[index] == "w":
                if string[index + 1] == "a":
                    if string[index + 2] == "t":
                        if string[index + 3] == "e":
                            if string[index + 4] == "r":
                                counter += 1

        if (len(string) - index) >= 4:
            if string[index] == "f":
                if string[index + 1] == "i":
                    if string[index + 2] == "s":
                        if string[index + 3] == "h":
                            counter += 1

        if (len(string) - index) >= 3:
            if string[index] == "s":
                if string[index + 1] == "u":
                    if string[index + 2] == "n":
                        counter += 1

    return counter


user_input = input().lower()
result = beach_counter(user_input)
print(result)
