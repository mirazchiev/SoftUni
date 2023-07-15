dictionary = {}

while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())
    if resource in dictionary:
        dictionary[resource] += quantity
    else:
        dictionary[resource] = quantity

for resource, quantity in dictionary.items():
    print(f"{resource} -> {quantity}")
