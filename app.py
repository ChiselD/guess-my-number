import random

secret_number = random.randint(1,101)

guess = int(input("Guess what number I'm thinking of (between 1 and 100): "))

while guess != secret_number:
	if guess > secret_number:
		guess = int(input("Too high! Guess again: "))
	if guess < secret_number:
		guess = int(input("Too low! Guess again: "))

if guess == secret_number:
	print(f"You guessed it! I was thinking of {secret_number}.")