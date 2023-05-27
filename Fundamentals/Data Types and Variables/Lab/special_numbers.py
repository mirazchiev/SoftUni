n = int(input())

for numbers in range(1, n+1):
    num_string = str(numbers)
    summed = 0
    for i in range(len(num_string)):
        num_integer = int(num_string[i])
        summed += num_integer
        is_special = summed == 5 or summed == 7 or summed == 11
    print(f"{numbers} -> {bool(is_special)}")
