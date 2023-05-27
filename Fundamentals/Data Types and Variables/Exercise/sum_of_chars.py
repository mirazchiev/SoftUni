n = int(input())

total = 0

for i in range(n):
    inputs = input()
    amount = ord(inputs)
    total += amount
print(f"The sum equals: {total}")
