def josephus_permutation(sequence: list, step: int):
    new_list = []
    index = 0
    while len(sequence) > 0:
        index = (index + step - 1) % len(sequence)
        new_list.append(sequence.pop(index))
    return f"[{','.join(new_list)}]"


numbers = input().split()
killing_step = int(input())
result = josephus_permutation(numbers, killing_step)
print(result)
