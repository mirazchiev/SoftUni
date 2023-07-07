def merge_elements(arr, start_index, end_index):
    if start_index < 0:
        start_index = 0
    if end_index >= len(arr):
        end_index = len(arr) - 1
    merged_string = ''.join(arr[start_index:end_index+1])
    arr[start_index:end_index+1] = [merged_string]
    return arr

def divide_element(arr, index, partitions):
    if index >= len(arr):
        return arr
    element = arr[index]
    substring_length = len(element) // partitions
    extra_length = len(element) % partitions
    substrings = [element[i:i+substring_length] for i in range(0, len(element)-extra_length, substring_length)]
    if extra_length > 0:
        substrings.append(element[-extra_length:])
    arr[index:index+1] = substrings
    return arr

# Read the input array
arr = input().split()

# Process the commands
while True:
    command = input().split()
    if command[0] == '3:1':
        break
    if command[0] == 'merge':
        start_index = int(command[1])
        end_index = int(command[2])
        arr = merge_elements(arr, start_index, end_index)
    elif command[0] == 'divide':
        index = int(command[1])
        partitions = int(command[2])
        arr = divide_element(arr, index, partitions)

# Print the resulting elements
print(' '.join(arr))
