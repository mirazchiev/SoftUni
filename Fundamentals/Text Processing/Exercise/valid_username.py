usernames = input().split(", ")

for username in usernames:
    helper_username = username.replace("-", "")
    helper_username = helper_username.replace("_", "")
    helper_username = helper_username.replace(" ", "@")
    if 3 <= len(username) <= 16 and helper_username.isalnum():
        print(username)
