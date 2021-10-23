import random
import os
from GlobalFunctions import delete_last_line
from Utils import screen_cleaner
user_guess_number = 0


# Function Generate number creates a global secret number for game
# Functions enters a random number between 1 - Difficulty number into secret number
def generate_number(difficulty_num: int):
    global secret_number
    secret_number = random.randint(1, difficulty_num)


# Function get guess from user gets the difficulty number and requests the user to enter a guess
# Function enters the user's guess into global UserGuess Number
def get_guess_from_user(difficulty_num: int):
    global user_guess_number

    # Run until user's number is between 1 - Difficulty number
    while user_guess_number < 1 or user_guess_number > difficulty_num:
        try:
            # Requests guess
            user_guess_number = int(input(f'please enter a number between 1 to {difficulty_num}\n'))
        except ValueError:
            # If user entered an invalid number
            # Delete user's guess and our request in order to reprint them
            delete_last_line()
            delete_last_line()
            print("Please enter a valid number.")


# Functions returns True / False according to check if UserGuessNumber  is equal to SecretNumber
def compare_results():
    return secret_number == user_guess_number


# Function Play is playing the Memory Game
# Function gets the difficulty number in order to pass it forward to other functions
# Function returns either "User Won" or "User Lost"
def play(difficulty_num:int):
    print("In Guess Game you will be required to guess the Secret Number")
    print("If your guess and secret number are the same you have won the game")

    # Input sentence just to get ENTER from user after he read the instructions
    Unused = input("press enter to continue")
    screen_cleaner()

    # Create Secret number
    generate_number(difficulty_num)

    # Asks the user to guess a number
    get_guess_from_user(difficulty_num)

    # Get results
    results = compare_results()

    # Clean the screen and starts printing the results
    _ = os.system('cls')
    print(f"The Secret number was {secret_number}\nUser guessed {user_guess_number}")
    if results:
        return "User Won"
    else:
        return "User Lost"
