money_as_string = input().split(", ")
beggars = int(input())

money_as_integer = []

for element in money_as_string:
    money_as_integer.append(int(element))
final_amounts = []
index = 0

while index < beggars:
    sum_beggar = 0
    for current_index in range(index, len(money_as_integer), beggars):
        sum_beggar += money_as_integer[current_index]
    final_amounts.append(sum_beggar)
    index += 1

print(final_amounts)