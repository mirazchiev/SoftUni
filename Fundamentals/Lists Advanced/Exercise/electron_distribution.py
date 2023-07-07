def electron_distribution(electrons: int) -> list:
    shells = []
    while True:
        if electrons <= 0:
            break
        shell = 2 * ((len(shells) + 1) ** 2)
        if electrons > shell:
            shells.append(shell)
            electrons -= shell
        else:
            shells.append(electrons)
            electrons -= electrons
    return shells


user_input = int(input())
result = electron_distribution(user_input)
print(result)
