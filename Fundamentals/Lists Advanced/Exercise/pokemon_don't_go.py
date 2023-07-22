pokemons = [int(pokemon) for pokemon in input().split()]
total = 0

while pokemons:
    index = int(input())
    if index < 0:
        index = 0
        for current_index, pokemon in enumerate(pokemons):
            if current_index == index:
                continue
            if pokemon <= pokemons[index]:
                pokemons[current_index] += pokemons[index]
            else:
                pokemons[current_index] -= pokemons[index]
        total += pokemons[0]
        pokemons[0] = pokemons[-1]
    elif index >= len(pokemons):
        index = len(pokemons) - 1
        for current_index, pokemon in enumerate(pokemons):
            if current_index == index:
                continue
            if pokemon <= pokemons[index]:
                pokemons[current_index] += pokemons[index]
            else:
                pokemons[current_index] -= pokemons[index]
        total += pokemons[-1]
        pokemons[-1] = pokemons[0]
    else:
        for current_index, pokemon in enumerate(pokemons):
            if current_index == index:
                continue
            if pokemon <= pokemons[index]:
                pokemons[current_index] += pokemons[index]
            else:
                pokemons[current_index] -= pokemons[index]
        total += pokemons.pop(index)

print(total)
