import re

items_list = []
total_cost = 0
pattern = r">>(\w+)<<(\d+|\d+\.?\d+)!(\d+)"
while True:
    command = input()
    if command == "Purchase":
        break

    matches = re.findall(pattern, command)
    if matches:
        matches = matches[0]
        items_list.append(matches[0])
        total_cost += float(matches[1]) * int(matches[2])

print("Bought furniture:")
for item in items_list:
    print(item)
print(f"Total money spend: {total_cost:.2f}")
