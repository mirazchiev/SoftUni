capacity = 255
n = int(input())

for i in range(n):
    liters = int(input())
    if (capacity - liters) < 0:
        print("Insufficient capacity!")
    else:
        capacity -= liters
print(255 - capacity)
