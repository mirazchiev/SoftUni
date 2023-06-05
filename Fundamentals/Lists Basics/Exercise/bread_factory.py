energy = 100
coins = 100

is_closed = False

events = input().split("|")
for event in events:
    event = event.split("-")
    current_event = event[0]
    current_points = int(event[1])
    if current_event == "rest":
        current_energy = current_points
        if energy + current_energy > 100:
            print(f"You gained {100 - energy} energy.")
            print(f"Current energy: {100}.")
        else:
            energy += current_energy
            print(f"You gained {current_energy} energy.")
            print(f"Current energy: {energy}.")
    elif current_event == "order":
        current_coins = current_points
        if energy >= 30:
            energy -= 30
            coins += current_coins
            print(f"You earned {current_coins} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        current_ingredient = current_event
        current_coins = current_points
        if coins >= current_coins:
            coins -= current_coins
            print(f"You bought {current_ingredient}.")
        else:
            print(f"Closed! Cannot afford {current_ingredient}.")
            is_closed = True
            break
if is_closed:
    pass
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
