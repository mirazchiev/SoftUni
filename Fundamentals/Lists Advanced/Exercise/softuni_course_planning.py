schedule = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break
    if "Add" in command:
        command = command.split(":")
        if command[1] not in schedule:
            schedule.append(command[1])
    if "Insert" in command:
        command = command.split(":")
        if command[1] not in schedule:
            schedule.insert(int(command[2]), command[1])
    if "Remove" in command:
        command = command.split(":")
        if command[1] in schedule:
            if command[1] + "-Exercise" in schedule:
                schedule.remove(command[1])
                schedule.remove(command[1] + "-Exercise")
            else:
                schedule.remove(command[1])
    if "Swap" in command:
        command = command.split(":")
        if command[1] in schedule and command[2] in schedule:
            index1 = schedule.index(command[1])
            index2 = schedule.index(command[2])
            if command[1] + "-Exercise" in schedule and command[2] + "-Exercise" in schedule:
                schedule[index1], schedule[index1 + 1], schedule[index2], schedule[index2 + 1]\
                    = schedule[index2], schedule[index2 + 1], schedule[index1], schedule[index1 + 1]
            elif command[1] + "-Exercise" in schedule:
                schedule[index1], schedule[index2] = schedule[index2], schedule[index1]
                schedule.insert(index2 + 1, schedule.pop(index1 + 1))
            elif command[2] + "-Exercise" in schedule:
                schedule[index1], schedule[index2] = schedule[index2], schedule[index1]
                schedule.insert(index1 + 1, schedule.pop(index2 + 1))
            else:
                schedule[index1], schedule[index2] = schedule[index2], schedule[index1]
    if "Exercise" in command:
        command = command.split(":")
        if command[1] in schedule:
            if command[1] + "-Exercise" not in schedule:
                index = schedule.index(command[1])
                schedule.insert(index + 1, command[1] + "-Exercise")
        else:
            schedule.append(command[1])
            schedule.append(command[1] + "-Exercise")

for i in range(len(schedule)):
    print(f"{i + 1}.{schedule[i]}")
