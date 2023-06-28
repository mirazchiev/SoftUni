food = float(input())
hay = float(input())
cover = float(input())
weight = float(input())

for day in range(1, 30 + 1):
    food -= 0.300
    if day % 2 == 0:
        hay -= 0.05 * food
    if day % 3 == 0:
        cover -= 1/3 * weight
if food <= 0 or hay <= 0 or cover <= 0:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
