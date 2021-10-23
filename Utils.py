import os

# Location of the exported WORLD OF GAMES folder
WORLD_OF_GAMES_LOCATION = "C:\\Users\\snimr\\PycharmProjects"

# Constants
# Scores file name - the file in which scores are kept
SCORES_FILE_NAME = WORLD_OF_GAMES_LOCATION + "\\WorldOfGames\\Level 3\\score.txt"

# bad return code - A number representing a bad return code for a function
BAD_RETURN_CODE=int("-1")


# Screen cleaner function
# a function that clears the screen
def screen_cleaner():
    clear_screen = os.system('cls')
    clear_screen()



