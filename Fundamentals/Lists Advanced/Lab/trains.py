def train(number_of_wagons: int):
    command = ''
    final_train = [0 for wagon in range(number_of_wagons)]
    while command != "End":
        command = input()
        if "add" in command:
            people = int(command[3:])
            final_train[-1] += people
        elif "insert" in command:
            command = command.split()
            index = int(command[1])
            people = int(command[2])
            final_train[index] += people
        elif "leave" in command:
            command = command.split()
            index = int(command[1])
            people = int(command[2])
            final_train[index] -= people
    return final_train


wagons = int(input())
result = train(wagons)
print(result)
