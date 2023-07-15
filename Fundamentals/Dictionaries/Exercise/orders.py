stock = {}

while True:
    command = input()
    if command == "buy":
        break
    name, price, quantity = command.split()
    if name not in stock:
        stock[name] = [float(price), int(quantity)]
    else:
        stock[name][0] = float(price)
        stock[name][1] += int(quantity)

for name, total_price in stock.items():
    print(f"{name} -> {total_price[0] * total_price[1]:.2f}")
