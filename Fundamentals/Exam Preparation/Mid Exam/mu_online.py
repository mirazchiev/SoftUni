health = 100
bitcoins = 0

dungeon = input().split("|")
for index, room in enumerate(dungeon):
    command_number = room.split()
    command = command_number[0]
    number = int(command_number[1])
    if "potion" in command:
        if number + health > 100:
            print(f"You healed for {100 - health} hp.")
            health = 100
            print(f"Current health: {health} hp.")
        else:
            print(f"You healed for {number} hp.")
            health += number
            print(f"Current health: {health} hp.")
    elif "chest" in command:
        print(f"You found {number} bitcoins.")
        bitcoins += number
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {index + 1}")
            break
if health > 0:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
