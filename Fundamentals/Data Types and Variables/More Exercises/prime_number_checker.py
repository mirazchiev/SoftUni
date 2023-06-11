def prime_check(number):
    if number > 1:
        for divisor in range(2, number):
            if number % divisor == 0:
                return False
        return True
    else:
        return "Invalid input!"


user_input = int(input())
result = prime_check(user_input)
print(result)
