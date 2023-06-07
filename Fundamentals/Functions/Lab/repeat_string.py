string = input()
counter = int(input())

repeat_string = lambda str, count: str * count
print(repeat_string(string, counter))
