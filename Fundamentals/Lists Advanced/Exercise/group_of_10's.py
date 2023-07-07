def groups(numbers: list) -> str:
    counter = 10
    while True:
        if not numbers:
            break
        print_numbers = []
        for index in range(len(numbers) - 1, - 1, - 1):
            if numbers[index] <= counter:
                print_numbers.append(numbers[index])
                numbers.pop(index)
        print(f"Group of {counter}'s: {list(reversed(print_numbers))}")
        counter += 10
    return "GJ"


user_input = list(map(int, input().split(", ")))
result = groups(user_input)
