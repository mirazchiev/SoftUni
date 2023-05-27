from random import randint

user_input = input("Choose [r]ock, [p]aper or [s]cissors:")

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

if user_input == "r":
    user_input = rock
elif user_input == "p":
    user_input = paper
elif user_input == "s":
    user_input = scissors
else:
    print("Invalid Input. Try again...")

computer_input = randint(1, 3)
if computer_input == "1":
    computer_input = rock
elif computer_input == "2":
    computer_input = paper
elif computer_input == "3":
    computer_input = scissors
print(f"The computer chose {computer_input}.")

if user_input == rock and computer_input == scissors\
    or user_input == scissors and computer_input == paper\
    or user_input == paper and computer_input == rock:
    print("You win!")
elif user_input == computer_input:
    print("Draw!")
else:
    print("You lose!")
