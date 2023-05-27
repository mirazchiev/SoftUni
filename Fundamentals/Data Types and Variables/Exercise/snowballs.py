n = int(input())
snowball_weight = 0
snowball_time = 0
snowball_value = 0
snowball_quality = 0

for snowball in range(n):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight / time) ** quality
    if value > snowball_value:
        snowball_weight = weight
        snowball_time = time
        snowball_value = value
        snowball_quality = quality

print(f"{int(snowball_weight)} : {int(snowball_time)} = {int(snowball_value)} ({int(snowball_quality)})")
