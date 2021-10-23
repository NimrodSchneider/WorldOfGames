from time import sleep
from GlobalFunctions import delete_last_line
from Utils import screen_cleaner
import random
import os


# Generate sequence gets the difficulty number of the game
# Function generates an array of random numbers between 1-101
# It does it by appending numbers to global array named MemoryGameArray
# Length of array is according to Difficulyt num
def generate_sequence(difficulty_num: int):
    global memory_game_array

    # For 1 till difficulty number
    for i in range(difficulty_num):
        # Append one random number from 1-101
        memory_game_array.append(random.randint(1, 101))


# get list from user gets the user's guess.
# Amount of numbers the users need to enter defined by Difficulty Number
# The function appends the numbers to global UserGuessArray
def get_list_from_user(difficulty_num: int):
    global user_guess_array
    print("Please enter the numbers you saw one by one")

    # While the user guess array is not the same length of the difficulty number
    while len(user_guess_array) < difficulty_num:
        try:
            # Request a number from user
            # Append that number to the array
            if len(user_guess_array) == 0:
                user_guess_array.append(int(input(f"Enter the 1st number\n")))
            elif len(user_guess_array) == 1:
                user_guess_array.append(int(input(f"Enter the 2st number\n")))
            elif  len(user_guess_array) == 2:
                user_guess_array.append(int(input(f"Enter the 3rd number\n")))
            else:
                user_guess_array.append(int(input(f"Enter the {len(user_guess_array) + 1}th number\n")))

        # User tried to insert an invalid value
        except ValueError:
            # Delete the last two sentences (our request and user's guess)
            delete_last_line()
            delete_last_line()
            print("please enter a valid number")


# Functions returns True / False according to check if UsersGuessArray is equal to MemoryGameArray
def is_list_equal():
    return memory_game_array == user_guess_array


# Function Play is playing the Memory Game
# Function gets the difficulty number in order to pass it forward to other functions
# Function returns either "User Won" or "User Lost"
def play(difficulty_num: int):
    print("In Memory Game a list of numbers will appear on the screen for 0.7 seconds")
    print("After list will disappear you will be required to enter your memorized list one number at a time")
    print("If both lists are equal you have won the game")

    # Input sentence just to get ENTER from user after he read the instructions
    unused = input("press enter to continue")
    screen_cleaner()

    # Gets the memory game array
    generate_sequence(difficulty_num)

    # Print the array for 0.7 seconds and then deletes it
    print(memory_game_array)
    sleep(0.7)
    delete_last_line()

    # Gets the user's guess
    get_list_from_user(difficulty_num)

    # Gets the results
    results = is_list_equal()

    # Clean the screen and starts printing the results
    _ = os.system('cls')
    print(f"The Memory game list was {memory_game_array}\nUser guessed {user_guess_array}")
    if results:
        return "User Won"
    else:
        return "User Lost"