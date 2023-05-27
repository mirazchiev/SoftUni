number_of_people = int(input())
capacity = int(input())

# if (number_of_people // capacity) < 1:
#     print("All the persons fit inside the elevator.")
#     print("Only one course is needed.")
# elif number_of_people % capacity == 0:
#     courses = number_of_people // capacity
#     print(f"{courses} courses * {capacity} people")
# else:
#     courses = number_of_people // capacity
#     people_left = number_of_people % capacity
#     print(f"{courses} courses * {capacity} people")
#     print(f"+ 1 course * {people_left} persons")

courses = number_of_people // capacity
people_left = number_of_people % capacity
if people_left > 0:
    print(courses + 1)
else:
    print(courses)
