print("Welcome to the guessing game!")
import random

a=int(input("Enter the starting range for the number to be guessed: "))
b = int(input("Enter the ending range number to be guessed: "))

x = random.randint(a,b)

guess_count = 0
max_guess  = 3

while guess_count < max_guess:
    guess = int(input("Enter your guess:"))
    guess_count += 1
    if guess == x:
        print(f"Congratulations! You guessed the correct number within {max_guess} attempts.")
        break   
else:
    print(f"Sorry, that's not the correct number. You have {max_guess - guess_count} attempts left.")
        