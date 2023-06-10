def palindrome_integers(integers):
    for integer in integers:
        is_palindrome = False
        integer_forward = int(integer)
        integer_backward = list(reversed(integer))
        integer_backward_list = []
        for digit in integer_backward:
            integer_backward_list.append(digit)
        integer_backward = "".join(integer_backward_list)
        integer_backward = int(integer_backward)
        if integer_forward == integer_backward:
            is_palindrome = True
        print(is_palindrome)


numbers = input().split(", ")
palindrome_integers(numbers)
