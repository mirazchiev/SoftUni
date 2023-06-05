list_of_integers = input().split()
number = int(input())
new_list_of_integers = []
final_list_of_integers = []

for integer in list_of_integers:
    new_integer = int(integer)
    new_list_of_integers.append(new_integer)
sorted_list_of_integers = sorted(new_list_of_integers, reverse=True)
for index_of_deleted_element in range(number):
    sorted_list_of_integers.pop()
for i in list_of_integers:
    if int(i) in sorted_list_of_integers:
        final_list_of_integers.append(i)
result = ", ".join(final_list_of_integers)
print(result)
