number_of_rooms = int(input())
total_chairs_left = 0
is_valid = True
for room in range(1, number_of_rooms + 1):
    chairs_visitors = input().split()
    chairs = len(chairs_visitors[0])
    visitors = int(chairs_visitors[1])
    chairs_left = chairs - visitors
    if chairs_left < 0:
        print(f"{abs(chairs_left)} more chairs needed in room {room}")
        is_valid = False
    else:
        total_chairs_left += chairs_left
if is_valid:
    print(f"Game On, {total_chairs_left} free chairs left")
