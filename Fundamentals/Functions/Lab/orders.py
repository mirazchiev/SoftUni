def orders(price, quantity):
    total_price = price * quantity
    return total_price


dictionary = {"coffee": 1.50, "water": 1.00, "coke": 1.40, "snacks": 2.00}
order = input()
qty = int(input())
print(f"{orders(dictionary[order], qty):.2f}")
