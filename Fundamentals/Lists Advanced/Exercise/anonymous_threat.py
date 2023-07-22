def merge_elements(list_of_strings, start_index, end_index):
    if start_index <= 0:
        start_index = 0
    if end_index >= len(list_of_strings):
        end_index = len(list_of_strings) - 1
    merged_string = ''.join(list_of_strings[start_index:end_index + 1])
    list_of_strings[start_index:end_index + 1] = [merged_string]
    return list_of_strings


def divide_element(list_of_strings, index, partitions):
    if index >= len(list_of_strings) or index < 0:
        return list_of_strings
    element = list_of_strings[index]
    substring_length = len(element) // partitions
    extra_length = len(element) % partitions
    substrings = [element[i:i+substring_length] for i in range(0, len(element)-extra_length, substring_length)]
    if extra_length > 0:
        substrings[-1] += element[-1]
    list_of_strings[index:index+1] = substrings
    return list_of_strings


strings = input().split()

while True:
    command = input().split()
    if command[0] == '3:1':
        break
    if command[0] == 'merge':
        start = int(command[1])
        end = int(command[2])
        strings = merge_elements(strings, start, end)
    elif command[0] == 'divide':
        user_index = int(command[1])
        user_partitions = int(command[2])
        strings = divide_element(strings, user_index, user_partitions)

print(' '.join(strings))
