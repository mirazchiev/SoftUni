students = int(input())
lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
max_attendance = 0
for student in range(students):
    attendance = int(input())
    total_bonus = attendance / lectures * (5 + additional_bonus)
    if total_bonus >= max_bonus:
        max_bonus = total_bonus
        max_attendance = attendance
print(f"Max Bonus: {max_bonus:.0f}.\nThe student has attended {max_attendance} lectures.")
