names_list = input().split(", ")
blacklisted_counter = 0
lost_counter = 0

while True:
    command = input()
    if command == "Report":
        break
    if "Blacklist" in command:
        command_name = command.split()
        name = command_name[1]
        if name in names_list:
            index = names_list.index(name)
            names_list.pop(index)
            names_list.insert(index, "Blacklisted")
            print(f"{name} was blacklisted.")
            blacklisted_counter += 1
        else:
            print(f"{name} was not found.")
    elif "Error" in command:
        command_index = command.split()
        index = int(command_index[1])
        # is_valid = 0 <= index and index < len(names_list)
        # is_not_blacklisted = names_list[index] != "Blacklisted"
        # is_not_lost = names_list[index] != "Lost"
        if 0 <= index and index < len(names_list) and names_list[index] != "Blacklisted" and names_list[index] != "Lost":
            name = names_list[index]
            names_list.pop(index)
            names_list.insert(index, "Lost")
            print(f"{name} was lost due to an error.")
            lost_counter += 1
    elif "Change" in command:  # if already blacklisted or lost?
        command_index_new_name = command.split()
        index = int(command_index_new_name[1])
        new_name = command_index_new_name[2]
        # is_valid = 0 <= index and index < len(names_list)
        # is_not_blacklisted = names_list[index] != "Blacklisted"
        # is_not_lost = names_list[index] != "Lost"
        if 0 <= index and index < len(names_list):
            old_name = names_list[index]
            names_list.pop(index)
            names_list.insert(index, new_name)
            print(f"{old_name} changed his username to {new_name}.")
    else:
        break
print(f"Blacklisted names: {blacklisted_counter}")
print(f"Lost names: {lost_counter}")
print(" ".join(names_list))
