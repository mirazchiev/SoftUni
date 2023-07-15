inventory = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False

while not obtained:
    raw_data = input().split()
    for index in range(0, len(raw_data), 2):
        quantity = int(raw_data[index])
        material = raw_data[index + 1].lower()
        if material not in inventory:
            inventory[material] = 0
        inventory[material] += quantity
        if material == "shards":
            if inventory[material] >= 250:
                inventory[material] -= 250
                print("Shadowmourne obtained!")
                obtained = True
                break
        elif material == "fragments":
            if inventory[material] >= 250:
                inventory[material] -= 250
                print("Valanyr obtained!")
                obtained = True
                break
        elif material == "motes":
            if inventory[material] >= 250:
                inventory[material] -= 250
                print("Dragonwrath obtained!")
                obtained = True
                break

for material, quantity in inventory.items():
    print(f"{material}: {quantity}")
