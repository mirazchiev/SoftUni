number_of_cars = int(input())
parking = {}

for car in range(number_of_cars):
    command = input().split()
    if "register" in command:
        username = command[1]
        license_plate = command[2]
        if username in parking:
            print(f"ERROR: already registered with plate number {license_plate}")
        else:
            parking[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
    else:
        username = command[1]
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            parking.pop(username)

for name, plate in parking.items():
    print(f"{name} => {plate}")
