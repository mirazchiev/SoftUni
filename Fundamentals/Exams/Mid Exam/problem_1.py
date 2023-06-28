number_of_cities = int(input())
total_profit = 0
total_expenses = 0

for city in range(1, number_of_cities + 1):
    additional_expense = 0
    name_of_the_city = input()
    income = float(input())
    expenses = float(input())
    if city % 5 == 0:
        income *= 0.9
    else:
        if city % 3 == 0:
            additional_expense = expenses * 0.5
    profit = income - expenses - additional_expense
    total_profit += profit
    print(f"In {name_of_the_city} Burger Bus earned {profit:.2f} leva.")
print(f"Burger Bus total profit: {total_profit:.2f} leva.")
