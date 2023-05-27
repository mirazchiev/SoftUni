budget = float(input())
flour_price_per_kg = float(input())
eggs_price_per_pack = flour_price_per_kg * 0.75
milk_price_per_quarter_of_a_liter = flour_price_per_kg * 1.25 / 4

money_needed_for_one_loaf_of_bread = flour_price_per_kg + eggs_price_per_pack + milk_price_per_quarter_of_a_liter
number_of_loaves = int(budget // money_needed_for_one_loaf_of_bread)
colored_eggs = number_of_loaves * 3
money_left = budget - number_of_loaves * money_needed_for_one_loaf_of_bread
for i in range(1, number_of_loaves + 1):
    if i % 3 == 0:
        colored_eggs -= (i - 2)

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs "
      f"and {money_left:.2f}BGN left.")
