

import random

def welcome():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

def generate_random_number():
    return random.randint(1, 100)

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Please enter a valid number.")

def evaluate_guess(secret_number, guess):
    if guess < secret_number:
        return "Too low!"
    elif guess > secret_number:
        return "Too high!"
    else:
        return "Congratulations! You've guessed the number!"

def play_game():
    welcome()
    secret_number = generate_random_number()
    attempts = 0

    while True:
        guess = get_user_guess()
        attempts += 1
        result = evaluate_guess(secret_number, guess)
        print(result)
        
        if result.startswith("Congratulations"):
            print("Number of attempts:", attempts)
            break

if __name__ == "__main__":
    play_game()


#welcome to Guess the Number!
#I'm thinking of a number between 1 and 100. Can you guess it?
#Enter your guess (between 1 and 100): 6
#Too low!
#Enter your guess (between 1 and 100): 70
#Too high!
#Enter your guess (between 1 and 100): 50
#congratulations! you've guessed the number!
#Number of attempts: 3
