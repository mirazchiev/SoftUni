gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break
    elif "OutOfStock" in command:
        command = command.split()
        gift = command[1]
        gifts = [replaced.replace(gift, "None") for replaced in gifts]
    elif "Required" in command:
        command = command.split()
        gift = command[1]
        gift_index = int(command[2])
        if 0 <= gift_index < len(gifts):
            gifts[gift_index] = gift
    elif "JustInCase" in command:
        command = command.split()
        gift = command[1]
        gifts[-1] = gift

result = ' '.join([gift for gift in gifts if gift != "None"])
print(result)
