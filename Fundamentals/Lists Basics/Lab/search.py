n = int(input())
word = input()

my_list = []

for i in range(n):
    strings = input()
    my_list.append(strings)

print(my_list)

new_list = []

for strings in my_list:
    if word in strings:
        new_list.append(strings)

print(new_list)
