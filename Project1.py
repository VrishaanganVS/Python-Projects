#Number Guessing game in Python
'''
First all we have to do is geenerate a random number and store it
Then we have to get user input for guessing the number
'''
import random
import math

random_number = random.randint(1,100)
print("A Number has been set by the system, The user may try to guess it now")

def user():
    nu = int(input("Enter number to guess:"))

def guess(nu,random_number):
        if nu == random_number:
            print("Guessed correct")
        elif nu<random_number:
            return "Guessed too small"
        else:
            return "Too high"

    