initial_energy = int(input())
distance = 0
wins = 0

while True:
    command = input()
    if command == "End of battle":
        print(f"Won battles: {wins}. Energy left: {initial_energy}")
        break
    else:
        distance = int(command)
        if initial_energy >= distance:
            wins += 1
            initial_energy -= distance
            if wins % 3 == 0:
                initial_energy += wins
        else:
            print(f"Not enough energy! Game ends with {wins} won battles and {initial_energy} energy")
            break
