#Number Guessing game in Python
'''
First all we have to do is geenerate a random number and store it
Then we have to get user input for guessing the number
'''
import random
import math

random_number = random.randint(1,100)
print("A Number has been set by the system, The user may try to guess it now")

u = int(input("Enter the number to guess"))

if u<random_number:
    print("Value smaller than number")
elif u>random_number:
    print("Value Greater than number")
elif u==random_number:
    print("Number Guessed")