forces = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if "|" in command:
        side, user = command.split(" | ")
        is_found = False
        for user_list in forces.values():
            if user in user_list:
                is_found = True
                break
        if not is_found:
            if side not in forces:
                forces[side] = []
            forces[side].append(user)
    else:
        user, side = command.split(" -> ")
        is_found = False
        for user_list in forces.values():
            if user in user_list:
                is_found = True
                break
        if not is_found:
            if side not in forces:
                forces[side] = []
            forces[side].append(user)
        else:
            for key, value in forces.items():
                if user in value:
                    forces[key].remove(user)
                    break
            if side not in forces:
                forces[side] = []
            forces[side].append(user)
        print(f"{user} joins the {side} side!")

for side, user_list in forces.items():
    if len(forces[side]) == 0:
        continue
    print(f"Side: {side}, Members: {len(forces[side])}")
    for user in user_list:
        print(f"! {user}")
