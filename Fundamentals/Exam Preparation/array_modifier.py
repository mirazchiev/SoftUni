numbers = list(map(int, input().split()))
command = ""
while command != "end":
    command = input()
    if "swap" in command:
        command = command.split()
        index1 = int(command[1])
        index2 = int(command[2])
        numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
    elif "multiply" in command:
        command = command.split()
        index1 = int(command[1])
        index2 = int(command[2])
        numbers[index1] = numbers[index1] * numbers[index2]
    elif "decrease" in command:
        numbers = [(lambda x: x - 1)(number) for number in numbers]

print(", ".join(map(str, numbers)))
