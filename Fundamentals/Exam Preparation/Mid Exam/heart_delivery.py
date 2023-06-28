houses = list(map(int, input().split("@")))
position = 0
counter = 0
while True:
    command = input()
    if command == "Love!":
        break
    jump_distance = command.split()
    distance = int(jump_distance[1])
    position += distance
    if position >= len(houses):
        position = 0
    if houses[position] <= 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        houses[position] -= 2
        if houses[position] <= 0:
            counter += 1
            print(f"Place {position} has Valentine's day.")
print(f"Cupid's last position was {position}.")
if counter >= len(houses):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(houses) - counter} places.")
