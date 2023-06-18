net = 0
tax = 0
gross = 0

while True:
    user_input = input()
    if user_input == "special":
        if gross == 0:
            print("Invalid order!")
        gross *= 0.9
        break
    elif user_input == "regular":
        if gross == 0:
            print("Invalid order!")
        break
    price = float(user_input)
    if price < 0:
        print("Invalid price!")
        continue
    if price == 0:
        print("Invalid order!")
        continue
    net += price
    tax += 0.2 * price
    gross += price + 0.2 * price

if gross != 0:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {net:.2f}$\n"
          f"Taxes: {tax:.2f}$\n"
          f"-----------\n"
          f"Total price: {gross:.2f}$")
