fires = input().split("#")
water = int(input())
effort = 0
total_fire = 0
cells = []
print("Cells:")
for fire in fires:
    fire = fire.split(" = ")
    level = fire[0]
    water_needed = int(fire[1])
    is_valid = False
    if level == "High" and 81 <= water_needed <= 125:
        is_valid = True
    elif level == "Medium" and 51 <= water_needed <= 80:
        is_valid = True
    elif level == "Low" and 1 <= water_needed <= 50:
        is_valid = True
    if is_valid:
        if water >= water_needed:
            water -= water_needed
            effort += water_needed * 0.25
            print(f"- {water_needed}")
            total_fire += water_needed
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
