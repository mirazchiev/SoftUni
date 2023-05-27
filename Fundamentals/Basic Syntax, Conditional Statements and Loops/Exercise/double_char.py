while True:
    strings = input()
    if strings == "End":
        break
    if strings == "SoftUni":
        continue
    for i in range(len(strings)):
        print(strings[i]+strings[i], end='')
    print("")
