def numbers(numbers_list: list):
    average = sum(numbers_list) / len(numbers_list)
    greater = [number for number in numbers_list if number > average]
    greater = list(map(str, sorted(greater, key=lambda x: -x)))
    if len(greater) >= 5:
        greater = greater[:5]
    elif len(greater) == 0:
        return "No"
    return " ".join(greater)


user_input = list(map(int, input().split()))
result = numbers(user_input)
print(result)
