# 49. Simulate a guessing game (user guesses a number until correct).
import random

secret = random.randint(1,100)
guess =0


while secret != guess:
    guess = int(input("Guess the number :"))

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print(" Congratulations! You guessed it right.")