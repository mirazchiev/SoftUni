from math import floor

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

if abs(x1) + abs(y1) <= abs(x2) + abs(y2):
    print(f"({floor(x1)}, {floor(y1)})")
else:
    print(f"({floor(x2)}, {floor(y2)})")
