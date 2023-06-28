days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
total = 0

for day in range(1, days + 1):
    total += daily_plunder
    if day % 3 == 0:
        bonus = daily_plunder * 0.5
        total += bonus
    if day % 5 == 0:
        total *= 0.7
if total >= expected_plunder:
    print(f"Ahoy! {total:.2f} plunder gained.")
else:
    percentage = total / expected_plunder * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")
