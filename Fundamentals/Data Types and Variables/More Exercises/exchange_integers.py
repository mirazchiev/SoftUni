def flipper(a: int, b: int):
    a_new = b
    b_new = a
    return f"Before:\na = {a}\nb = {b}\nAfter:\na = {a_new}\nb = {b_new}"


num1 = int(input())
num2 = int(input())
result = flipper(num1, num2)
print(result)
