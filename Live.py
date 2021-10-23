from GuessGame import play as GuessGamePlay
from MemoryGame import play as MemoryGamePlay
from CurrencyRoulettePlay import play as CurrencyRoulettePlay
from Score import add_score
import os


# Game dictionary to print proper name and not number
GamesDict = {
    1: {"name": "Memory game", "desc": "a sequence of numbers will appear for 1 second and you have to guess it back"},
    2: {"name": "Guess game", "desc": "guess a number and see if you chose like the computer"},
    3: {"name": "Currency Roulette", "desc": "try and guess the value of a random amount of USD in ILS"}}


# Function welcome print a hello message to new player to the world of games
# Function gets a string value representing the player name
# Function prints a message to the screen
def welcome(name: str):
    return f"Hello {name} and welcome to the World of Games (WoG)\nHere you can find many cool games to play\n"


# Function Load_Game offers the player info about games present in world of Games
# Player chooses between 3 games:
# 1. Memory game - a sequence of numbers will appear for 1 second and you have to guess it back
# 2. Guess game - guess a number and see if you chose like the computer
# 3. Currency roulette - try and guess the value of a random amount of USD in ILS
# When user enters valid information , functions prints chosen game and chosen difficulty
def load_game():
    chosen_game = 0
    chosen_difficulty = 0

    # Run till user entered valid information
    while chosen_game not in GamesDict.keys():
        print("Please choose a game to play:")
        for Key in GamesDict.keys():
            print(f"{Key}. {GamesDict[Key]['name']} - {GamesDict[Key]['desc']}")

        # Try block to make sure user is not entering invalid information
        try:
            # Letting the user choose game
            chosen_game = int(input("Chosen game is : "))
            # Cleaning the screen of terminal
            _ = os.system('cls')

        # User entered invalid information
        except ValueError:
            _ = os.system('cls')
            print("Invalid Value. Please enter only integer number according to instructions\n")

        # User entered valid information in regards of Data Type
        else:
            # Check if the number entered for game is valid
            if chosen_game in [1, 2, 3]:
                continue
            # Game number is invalid
            else:
                print("Invalid Value. Please enter a valid game number\n\n")

    while chosen_difficulty not in [1, 2, 3, 4, 5]:
        # Try block to make sure user is not entering invalid information
        try:
            # Letting the user choose game and difficulty
            chosen_difficulty = int(input("Please choose game difficulty from 1 to 5:"))
            # Cleaning the screen of terminal
            _ = os.system('cls')

            # User entered invalid information
        except ValueError:
            _ = os.system('cls')
            print("Invalid Value. Please enter only integer number according to instructions\n")

        if chosen_difficulty in [1, 2, 3, 4, 5]:
            # All information is valid
            print(f"You have chosen to play {GamesDict[chosen_game]['name']} at difficulty {chosen_difficulty}")

        # Difficulty is invalid
        else:
            print("Invalid Value. Please enter a valid difficulty number\n\n")

    # Call relevant game and receiving its results
    if chosen_game == 1:
        game_result = MemoryGamePlay(chosen_difficulty)
    elif chosen_game == 2:
        game_result = GuessGamePlay(chosen_difficulty)
    elif chosen_game == 3:
        game_result = CurrencyRoulettePlay(chosen_difficulty)

    # print game results
    print(game_result)

    # if user won the game call the add_score function to add his scoring to the scores file
    if game_result == "User Won":
        add_score(int(chosen_difficulty))
