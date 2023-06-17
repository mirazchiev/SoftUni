command = ""
notes = [0] * 10
while True:
    command = input()
    if command == "End":
        break
    command = command.split("-")
    importance = int(command[0]) - 1
    note = command[1]
    notes.pop(importance)
    notes.insert(importance, note)
notes = [element for element in notes if element != 0]
print(notes)
