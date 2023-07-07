old_version = list(map(int, input().split(".")))
if old_version[2] == 9:
    if old_version[1] == 9:
        new_version = [old_version[0] + 1, 0, 0]
    else:
        new_version = [old_version[0], old_version[1] + 1, 0]
else:
    new_version = [old_version[0], old_version[1], old_version[2] + 1]

print(".".join(map(str, new_version)))
