def tribonacci():
    tribonacci_number = 1
    tribonacci_number_list = []
    for index in range(int(input())):
        if index == 0:
            tribonacci_number_list.append(tribonacci_number)
        elif index == 1:
            tribonacci_number_list.append(tribonacci_number)
        elif index == 2:
            tribonacci_number += 1
            tribonacci_number_list.append(tribonacci_number)
        else:
            tribonacci_number += tribonacci_number_list[index - 2] + tribonacci_number_list[index - 3]
            tribonacci_number_list.append(tribonacci_number)
    return " ".join(map(str, tribonacci_number_list))


result = tribonacci()
print(result)
