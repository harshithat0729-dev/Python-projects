import random

number = random.randint(1, 100)
attempts = 0

print("===== NUMBER GUESSING GAME =====")
print("Guess a number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

    if guess == number:
        print("Correct!")
        print("You guessed it in", attempts, "attempts.")
        break

    elif guess < number:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")
