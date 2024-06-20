# number_guessing_game.py

import random

def get_random_number():
    """Get a random number between 1 and 100"""
    return random.randint(1, 100)

def get_user_guess():
    """Get the user's guess"""
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def play_game():
    """Play the number guessing game"""
    number_to_guess = get_random_number()
    attempts = 0

    while True:
        guess = get_user_guess()
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break

def main():
    play_game()

if __name__ == '__main__':
    main()
