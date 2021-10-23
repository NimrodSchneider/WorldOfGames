from GlobalFunctions import get_currency
from GlobalFunctions import delete_last_line
from Utils import screen_cleaner
import random


# Function get money interval calculates the Money Interval for the user's guess
# Function gets the difficulty number and the Total Money in Dollars
# The function returns array with minimum and maximum for the interval
# The array is made of [Money in Shekels - (5 - Difficulty), Money in Shekels + (5 - Difficulty)
def get_money_interval(difficulty_num: int, total_money: int):

    # Users global function get_currency in order to gain the current USD to ILS currency rate
    exchange_rate = get_currency()

    # Calculates how much is the total money in shekels
    total_money_in_shekels = total_money * exchange_rate

    # Returns the array with minimum and maximum of the money interval
    return [total_money_in_shekels - (5 - difficulty_num), total_money_in_shekels + (5 - difficulty_num)]


# Function get guess from user gets the user's guess
# Function gets Total number in USD
# Function requests the user to assess how much is the total money in Shekels?
# Function returns user's guess
def get_guess_from_user(total_money: int):

    # User guess number is 0 until providing actual number
    user_guess_number = 0
    while user_guess_number == 0:
        try:
            # Get user guess
            user_guess_number = float(input(F"How many Shekels do you think are {total_money}$ are?\n"))
        except ValueError:
            # User entered invalid value
            # Delete User's guess and our request to reprint it
            delete_last_line()
            delete_last_line()
            print("Please enter a valid number")

    # Returns the user's guess
    return user_guess_number


# Function Play is playing the Memory Game
# Function gets the difficulty number in order to pass it forward to other functions
# Function returns either "User Won" or "User Lost"
def play(difficulty_num: int):
    print("In Currency Roulette you will have to guess how many shekels are the displayed USD amount")
    print("The higher the difficulty the more precise guess you will be required to give")
    print("if you guessed correctly or within the accepted range you will win the game")

    # Input sentence just to get ENTER from user after he read the instructions
    unused = input("press enter to continue")
    screen_cleaner()

    # Get random number between 1-100
    total_money_in_usd = random.randint(1, 100)

    # Get the interval numbers for the game
    money_interval = get_money_interval(difficulty_num, total_money_in_usd)

    # Get the user's guess
    user_guess_number = get_guess_from_user(total_money_in_usd)

    # Clean the screen and starts printing the results
    _ = os.system('cls')
    print(f"You had to guess a number between {money_interval[0]} to {money_interval[1]}")
    print(f"You guessed {user_guess_number}")
    if money_interval[0] <= user_guess_number <= money_interval[1]:
        return "User Won"
    else:
        return "User Lost"
