companies = {}

while True:
    command = input()
    if command == "End":
        break
    name, id = command.split(" -> ")
    if name not in companies:
        companies[name] = []
    if id not in companies[name]:
        companies[name].append(id)

for company, users in companies.items():
    print(company)
    for user in users:
        print(f"-- {user}")
