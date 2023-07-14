stock = input().split()

stock_dict = {}

for i in range(0, len(stock), 2):
    product = stock[i]
    quantity = int(stock[i + 1])
    stock_dict[product] = quantity

search = input().split()
for product_searched in search:
    if product_searched in stock:
        print(f"We have {stock_dict[product_searched]} of {product_searched} left")
    else:
        print(f"Sorry, we don't have {product_searched}")
