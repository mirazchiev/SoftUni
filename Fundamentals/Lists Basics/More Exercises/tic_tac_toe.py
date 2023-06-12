def tic_tac_toe(first_row: list, second_row: list, third_row: list):
    p1 = int(first_row[0])
    p2 = int(first_row[1])
    p3 = int(first_row[2])
    p4 = int(second_row[0])
    p5 = int(second_row[1])
    p6 = int(second_row[2])
    p7 = int(third_row[0])
    p8 = int(third_row[1])
    p9 = int(third_row[2])
    if p1 == 1 and p2 == 1 and p3 == 1 or p4 == 1 and p5 == 1 and p6 == 1 or p7 == 1 and p8 == 1 and p9 == 1 or \
            p1 == 1 and p4 == 1 and p7 == 1 or p2 == 1 and p5 == 1 and p8 == 1 or p3 == 1 and p6 == 1 and p9 == 1 or \
            p1 == 1 and p5 == 1 and p9 == 1 or p3 == 1 and p5 == 1 and p7 == 1:
        return "First player won"

    elif p1 == 2 and p2 == 2 and p3 == 2 or p4 == 2 and p5 == 2 and p6 == 2 or p7 == 2 and p8 == 2 and p9 == 2 or \
            p1 == 2 and p4 == 2 and p7 == 2 or p2 == 2 and p5 == 2 and p8 == 2 or p3 == 2 and p6 == 2 and p9 == 2 or \
            p1 == 2 and p5 == 2 and p9 == 2 or p3 == 2 and p5 == 2 and p7 == 2:
        return "Second player won"

    else:
        return "Draw!"


user_input_first_row = input().split()
user_input_second_row = input().split()
user_input_third_row = input().split()
result = tic_tac_toe(user_input_first_row, user_input_second_row, user_input_third_row)
print(result)
