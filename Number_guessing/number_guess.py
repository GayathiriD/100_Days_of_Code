from art import  logo # Importing logo from art module

import random

print(logo)  # Print the logo to the console

# Welcome message to the player
print("Welcome to Number Guessing Game")
print("I'm thinking of a number between 1 and 100")  
# Randomly generate a number between 1 and 100 for the computer
computer_guess = random.randint(1, 100)

# Ask the player to choose a difficulty level
mode = input("Choos a difficulty type 'easy' or 'hard' ")  # Typo: 'Choos' should be 'Choose'

# Function to handle the 'easy' mode
def easy(mode):
    attempt_easy = 10  # Set number of attempts for easy mode
    if mode.lower() == 'easy':  # Check if user selected easy
        while attempt_easy > 0:
            print(f"You have {attempt_easy} remaining to guess the number")
            human_guess = int(input("Make a guess: "))  # Take user input

            # Provide feedback based on the guess
            if human_guess > computer_guess:
                print("Too High \n Guess again")
                attempt_easy -= 1  # Reduce attempts
            elif human_guess < computer_guess:
                print("Too Low \n Guess again")
                attempt_easy -= 1  # Reduce attempts
            else:
                print(f"You got it.\n you guess {human_guess} and computer  guess {computer_guess} ")  # Correct guess
                break  # Exit loop if correct

            # If all attempts are used, inform the user
            if attempt_easy == 0:
                print(f"You've run out of guesses. You lose.\nComputer guess: {computer_guess}")

# Function to handle the 'hard' mode
def hard(mode):
    if mode.lower() == 'hard':  # Check if user selected hard
        attempt_hard = 5  # Set number of attempts for hard mode
        while attempt_hard > 0:
            print(f"You have {attempt_hard} remaining to guess the number")
            human_guess = int(input("Make a guess: "))  # Take user input

            # Provide feedback based on the guess
            if human_guess > computer_guess:
                print("Too High \n Guess again")
                attempt_hard -= 1  # Reduce attempts
            elif human_guess < computer_guess:
                print("Too Low \n Guess again")
                attempt_hard -= 1  # Reduce attempts
            else:
                print("You got it.\n you guess {human_guess} and computer  guess {computer_guess}")  # Correct guess
                break  # Exit loop if correct

        # If all attempts are used, inform the user
        if attempt_hard == 0:
            print(f"You've run out of guesses. You lose.\nComputer guess: {computer_guess}")

# Call the appropriate function based on selected difficulty
easy(mode)
hard(mode)
