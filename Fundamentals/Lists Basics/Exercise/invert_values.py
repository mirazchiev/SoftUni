list_of_numbers = input().split(" ")
opposite_numbers = []

for i in list_of_numbers:
    number = -int(i)
    opposite_numbers.append(number)

print(opposite_numbers)
