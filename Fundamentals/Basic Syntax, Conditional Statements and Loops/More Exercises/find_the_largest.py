number = list(input())
number.sort(reverse=True)
for digit in range(len(number)):
    print(number[digit], end="")
