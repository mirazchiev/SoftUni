group = int(input())
days = int(input())

coins = 0

for day in range(1, days+1):
    coins += 50
    if day % 10 == 0:
        group -= 2
    if day % 15 == 0:
        group += 5
    food = 2 * group
    coins -= food
    if day % 3 == 0:
        water = 3 * group
        coins -= water
    if day % 5 == 0:
        monster = 20 * group
        coins += monster
        if day % 3 == 0:
            party = 2 * group
            coins -= party
print(f"{group} companions received {coins // group} coins each.")
