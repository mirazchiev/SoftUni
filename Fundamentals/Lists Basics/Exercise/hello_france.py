ticket_price = 150
items = input().split("|")
budget = float(input())

list_of_items = []
profit = 0

for item in items:
    item = item.split("->")
    type_of_item = item[0]
    price_of_item = float(item[1])
    if type_of_item == "Clothes" and price_of_item > 50 \
            or type_of_item == "Shoes" and price_of_item > 35 \
            or type_of_item == "Accessories" and price_of_item > 20.50:
        continue
    else:
        if budget >= price_of_item:
            budget -= price_of_item
            selling_price = price_of_item * 1.40
            list_of_items.append(selling_price)
            profit += selling_price - price_of_item
print(' '.join([f"{selling_price:.2f}" for selling_price in list_of_items]))
print(f'Profit: {profit:.2f}')
total_left = budget + sum(list_of_items)
if total_left >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
