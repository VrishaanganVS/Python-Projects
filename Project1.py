#Number Guessing game in Python
'''
First all we have to do is geenerate a random number and store it
Then we have to get user input for guessing the number
'''
import random
import math

max_attempts= 10
random_number = random.randint(1,100)
print("A Number has been set by the system, The user may try to guess it now")

def user():
    nu = int(input("Enter number to guess:"))

def guess(nu,random_number):
    while nu != random_number:
        if nu == random_number:
            print("Guessed correct")
        elif nu<random_number:
            print("Guessed too small")
            guess = int(input("Enter number again:"))
        else:
            print("Too high")
            guess = int(input("Enter number again:"))


def att():
    attempts = 0
    won = False
   
    while attempts < max_attempts:
        attempts+= 1
        myg= guess()