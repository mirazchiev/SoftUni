moves = 0
sequence = list(input().split())
while True:
    command = input()
    if command == "end":
        print(f"Sorry you lose :(\n"
              f"{' '.join(sequence)}")
        break
    moves += 1
    command_list = command.split()
    index1 = int(command_list[0])
    index2 = int(command_list[1])
    if index1 > index2:
        index1, index2 = index2, index1
    if index1 == index2 or index1 < 0 or index2 < 0 or index1 >= len(sequence) or index2 >= len(sequence):
        sequence.insert(len(sequence) // 2, f"-{moves}a")
        sequence.insert(len(sequence) // 2, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
    else:
        if sequence[index1] == sequence[index2]:
            print(f"Congrats! You have found matching elements - {sequence.pop(index1)}!")
            sequence.pop(index2 - 1)
            if len(sequence) == 0:
                print(f"You have won in {moves} turns!")
                break
        else:
            print("Try again!")
