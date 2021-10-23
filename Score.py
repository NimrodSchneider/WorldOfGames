import Utils


# get_score is a function to get the information from the scores file
def get_score():
    try:
        # Read the scores file
        with open(Utils.SCORES_FILE_NAME, "r") as scores_file:
            # return the current score in the scores file
            return scores_file.read()

    # Got error while opening the file
    except BaseException as ex:
        return Utils.BAD_RETURN_CODE


# Update the scores file according to the difficulty number of the game the user won.
def add_score(difficulty_num: int):
    # Set the function global current score parameter
    global current_score

    # Gets score from the function Get_score
    current_score = int(get_score())

    # if function get_score failed
    if current_score == Utils.BAD_RETURN_CODE:
        # assign the result of difficulty number * 3 + 5
        current_score = difficulty_num * 3 + 5
    else:
        # Add the result of difficulty num * 3 + 5 to the current score in the file
        current_score = current_score + (difficulty_num * 3 + 5)

    try:
        # Write the new score to the file
        with open(Utils.SCORES_FILE_NAME, "w") as scores_file:
            scores_file.write(str(current_score))

    # Got error while opening the file
    except BaseException as ex:
        print(ex)

