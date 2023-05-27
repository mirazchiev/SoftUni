number_of_messages = int(input())
code = 0
message = ""

for i in range(number_of_messages):
    code = int(input())
    if code == 88:
        message = "Hello"
    elif code == 86:
        message = "How are you?"
    elif code < 88:
        message = "GREAT!"
    else:
        message = "Bye."
    print(message)
