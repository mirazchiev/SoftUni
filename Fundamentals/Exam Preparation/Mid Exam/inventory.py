items = input().split(", ")
while True:
    command = input()

    if command == "Craft!":
        print(", ".join(items))
        break
    task_item = command.split(" - ")
    task = task_item[0]
    item = task_item[1]

    if task == "Collect":
        if item not in items:
            items.append(item)

    if task == "Drop":
        if item in items:
            items.remove(item)

    if task == "Combine Items":
        old_item_new_item = item.split(":")
        old_item = old_item_new_item[0]
        new_item = old_item_new_item[1]
        if old_item in items:
            items.insert(items.index(old_item) + 1, new_item)

    if task == "Renew":
        if item in items:
            items.remove(item)
            items.append(item)
