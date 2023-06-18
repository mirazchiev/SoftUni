employee1_students_per_hour = int(input())
employee2_students_per_hour = int(input())
employee3_students_per_hour = int(input())
total_rate_per_hour = employee1_students_per_hour + employee2_students_per_hour + employee3_students_per_hour
student_count = int(input())
counter = 0
total_hours = 0

while True:
    if student_count <= 0:
        break
    else:
        counter += 1
        if counter % 4 == 0:
            total_hours += 1
            continue
        student_count -= total_rate_per_hour
        total_hours += 1

print(f"Time needed: {total_hours:.0f}h.")
