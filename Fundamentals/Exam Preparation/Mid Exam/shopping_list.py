groceries = input().split("!")
while True:
    command = input()
    if command == "Go Shopping!":
        print(", ".join(groceries))
        break

    if "Urgent" in command:
        urgent_item = command.split()
        item = urgent_item[1]
        if item in groceries:
            continue
        else:
            groceries.insert(0, item)

    elif "Unnecessary" in command:
        unnecessary_item = command.split()
        item = unnecessary_item[1]
        if item not in groceries:
            continue
        else:
            groceries.remove(item)

    elif "Correct" in command:
        correct_items = command.split()
        old_item = correct_items[1]
        new_item = correct_items[2]
        if old_item not in groceries:
            continue
        else:
            groceries[groceries.index(old_item)] = new_item

    elif "Rearrange" in command:
        rearrange_item = command.split()
        item = rearrange_item[1]
        if item not in groceries:
            continue
        else:
            groceries.remove(item)
            groceries.append(item)
