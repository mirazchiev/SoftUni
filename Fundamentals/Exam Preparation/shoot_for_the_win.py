def shooting_range(target: list):
    count = 0
    while True:
        command = input()
        if command == "End":
            return f"Shot targets: {count} -> {' '.join(map(str, target))}"
        shot = int(command)
        if 0 > shot or shot > len(target) - 1:
            continue
        if target[shot] == -1:
            continue
        else:
            count += 1
            shot_target = target[shot]
            updated_targets = []
            for index, target_index in enumerate(target):
                if target[index] != -1:
                    if target_index > shot_target:
                        updated_targets.append(target_index - shot_target)
                    else:
                        updated_targets.append(target_index + shot_target)
                else:
                    updated_targets.append(target_index)
            target = updated_targets
            target[shot] = -1


target_input = list(map(int, input().split()))
result = shooting_range(target_input)
print(result)
