# Omar Alabdalla: 2/14/2022 : This program is used for checking whether a number is positive, negative, or a zero.

# if statement: if: Checks to see if an argument is true or not.
# else if statement: elif: Checks to see if another argument is true or not besides the base if statement.
# else statements: Checks to see if none of the arguments are passed.
# For statements: Tries to set a loop for a limited amount of time. Most commonly used for counting.
# While loop: Continuously repeats loop until the argument is meant. Best used for repeating until user quits.

import random


def positiveChecker():
    while True:
        try:
            response = int(input("Please input an integer to determine whether its a positive or a negative: "
                                 "If you want to break free input any other type of variable: "))
            if response > 0:
                print("Your response is a positive")
            elif response < 0:
                print("Your response is a negative")
            else:
                print("Your response is a zero")
        except ValueError:
            print("You have chosen to quit")
            break


def rockPaperScissors():
    try:
        user_input = int(input("Do you want to play? \n 1: Yes 2: No \n"))
        while user_input != -1:
            user_input = int(input("Please input 0: rock, 1: Paper, 2: Scissors -1: To quit: "))
            ai_choice = random.randint(0, 2)
            if user_input == ai_choice:
                print("It's a Tie!")
            elif user_input == 0 and ai_choice == 2:
                print("You Win!")
            elif user_input == 0 and ai_choice == 1:
                print("You Lose!")
            elif user_input == 1 and ai_choice == 0:
                print("You Win!")
            elif user_input == 1 and ai_choice == 2:
                print("You Lose!")
            elif user_input == 2 and ai_choice == 1:
                print("You Win!")
            elif user_input == 2 and ai_choice == 0:
                print("You Lose!")
            elif user_input == -1:
                print("Goodbye!")
            else:
                print("You didn't input a proper value")
    except ValueError:
        print("You didn't input anything")


firstInput = bool(input('''Please input any variable if you want to check whether your number is positive or negative.
Input nothing if you want to play Rock Paper Scissor: '''))
if firstInput:
    positiveChecker()
else:
    rockPaperScissors()
