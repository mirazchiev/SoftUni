def wolf(animals: list):
    if animals[0] == "wolf":
        return "Please go away and stop eating my sheep"
    for index, animal in enumerate(animals):
        if animal == "wolf":
            sheep = index
    return f"Oi! Sheep number {sheep}! You are about to be eaten by a wolf!"


animals_list = list(reversed(input().split(", ")))
print(wolf(animals_list))
