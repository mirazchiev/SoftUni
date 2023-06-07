def calculator(operation, a, b):
    if operation == "multiply":
        return a * b
    if operation == "divide":
        return a / b
    if operation == "add":
        return a + b
    if operation == "subtract":
        return a - b


operation = input()
a = int(input())
b = int(input())

print(int(calculator(operation, a, b)))
