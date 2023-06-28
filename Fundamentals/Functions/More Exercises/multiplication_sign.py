def multiplication_sign():
    number1 = int(input())
    number2 = int(input())
    number3 = int(input())
    if number1 == 0 or number2 == 0 or number3 == 0:
        return "zero"
    negatives = 0
    if number1 < 0:
        negatives += 1
    if number2 < 0:
        negatives += 1
    if number3 < 0:
        negatives += 1
    if negatives % 2 == 0:
        return "positive"
    else:
        return "negative"


print(multiplication_sign())
