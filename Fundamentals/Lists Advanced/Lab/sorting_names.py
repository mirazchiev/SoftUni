def sorting_names(list_of_names: list):
    sorted_names = sorted(list_of_names, key=lambda x: (-len(x), x))

    return sorted_names


user_input = input().split(", ")
result = sorting_names(user_input)
print(result)
