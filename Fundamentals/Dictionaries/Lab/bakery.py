elements = input().split()

bakery = {}

for i in range(0, len(elements), 2):
    product = elements[i]
    quantity = int(elements[i + 1])
    bakery[product] = quantity

print(bakery)
