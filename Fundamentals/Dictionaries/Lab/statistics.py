stock = {}

while True:
    command = input().split(": ")
    if "statistics" in command:
        break
    for i in range(0, len(command), 2):
        product = command[i]
        quantity = int(command[i + 1])
        if product in stock:
            stock[product] += quantity
        else:
            stock[product] = quantity

print("Products in stock:")
for (product, quantity) in stock.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(stock)}")
print(f"Total Quantity: {sum(stock.values())}")
