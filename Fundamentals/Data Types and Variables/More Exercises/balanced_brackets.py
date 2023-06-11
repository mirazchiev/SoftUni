def balanced(n):
    opened = False
    closed = False
    for index in range(n):
        user_input = input()
        if user_input == "(":
            if opened:
                return "UNBALANCED"
            opened = True
        if user_input == ")":
            if not opened or closed:
                return "UNBALANCED"
            closed = True
        if opened and closed:
            opened = False
            closed = False
    return "BALANCED"


number_of_lines = int(input())
result = balanced(number_of_lines)
print(result)
