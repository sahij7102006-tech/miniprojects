#number guessing game -computer picks a random number,USER guesses with hints like "too high/too low",tracks number of attrmpts. usinig variable,loops ,conditionals,strings in python

import random

# Computer picks a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0
guess = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Loop until the user guesses correctly
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations!")
        print("You guessed the number:", secret_number)
        print("Number of attempts:", attempts)
