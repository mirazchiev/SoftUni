quantity = int(input())
days = int(input())

ornament_price = 2
ornament_points = 5
skirt_price = 5
skirt_points = 3
garland_price = 3
garland_points = 10
lights_price = 15
lights_points = 17
total_price = 0
total_points = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_price += ornament_price * quantity
        total_points += ornament_points
    if day % 3 == 0:
        total_price += (skirt_price + garland_price) * quantity
        total_points += (skirt_points + garland_points)
    if day % 5 == 0:
        total_price += lights_price * quantity
        total_points += lights_points
        if day % 3 == 0:
            total_points += 30
    if day % 10 == 0:
        total_points -= 20
        total_price += skirt_price + garland_price + lights_price

if days % 10 == 0:
    total_points -= 30

print(f'Total cost: {total_price}')
print(f'Total spirit: {total_points}')
