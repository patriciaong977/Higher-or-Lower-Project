# First time using pylint.

""" Importing Modules """
import random
from os import system, name
from gameData import data
from gameArt import logo, vs


### Functions ###
def clear():
    """ Clears the screen"""
    if name == 'nt':  # For windows
        _ = system('cls')
    else:  # For Unix and Linux
        _ = system('clear')

def get_random_ig():
    """ Returns a random IG account from the data list."""
    return random.choice(data)

def format_data(ig_data):
    """ Returns the account data into printable format."""
    ig_name = ig_data["name"]  # Access the name key.
    description = ig_data["description"]  # Access the description key.
    country = ig_data["country"]  # Access the country key.

    return f"{ig_name}, a {description}, from {country}" # Return the formatted string.
def check_answer(usr_guess, acc_1_followers, acc_2_followers):
    """ Checks the user's guess. """
    if acc_1_followers > acc_2_followers:
        return usr_guess == "1"
    else:
        return usr_guess == "2"


def start_game():
    """ Starts the game."""
    print(logo) # Print the logo

    ### Variables ###
    usr_score = 0  # Set the user score to 0
    game_over = False  # Game over is not True.
    ig_1 = get_random_ig()  # Setting the first IG account.
    ig_2 = get_random_ig()  # Setting the second IG account.


    while not game_over:  # While loop executes as long as its True.
        # Keep putting first account in second account, then get a new second account.
        ig_1 = ig_2
        ig_2 = get_random_ig()

        # Just in case the first account is the same as the second account.
        while ig_1 == ig_2:
            ig_2 = get_random_ig()

        # Print the first account.
        print(f"First account: {format_data(ig_1)}\n")
        print(vs)  # Print the vs logo.
        print(f"\nSecond account: {format_data(ig_2)}")

        # Ask the user for a guess.
        usr_guess = input("Who has more followers? Type '1' or '2': ")
        # Take the follower count from the data.
        acc_1_followers = ig_1["follower_count"]  # Access the follower_count key.
        acc_2_followers = ig_2["follower_count"]

        # Check if the user's guess is correct.
        is_correct = check_answer(usr_guess, acc_1_followers, acc_2_followers)

        clear()  # Clear the screen.
        print(logo)  # Print the logo.

        # If the user's guess is correct.
        if is_correct:
            usr_score = usr_score + 1  # Add 1 to the user's score.
            print(f"Correct! Your current score is {usr_score}.\n")
        else:
            game_over = True  # End the game.
            print(f"Your guess is incorrect. \n Game Over! \n Your final score is {usr_score}.")


### Start the Game ###
start_game()
