languages = {}
users = {}

while True:
    command = input().split("-")
    if len(command) == 1:
        break
    if len(command) == 2:
        username = command[0]
        del users[username]
        continue
    username, language, points = command
    if username not in users:
        users[username] = int(points)
    else:
        if users[username] <= int(points):
            users[username] = int(points)

    if language not in languages:
        languages[language] = 0
    languages[language] += 1

print("Results:")
for user, points in users.items():
    print(f"{user} | {points}")
print("Submissions:")
for language, count in languages.items():
    print(f"{language} - {count}")
