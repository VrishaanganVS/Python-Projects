import random
print("Rock paper scissor game!!")

a = input("Enter your choice (rock, paper, or scissor): ")


choices = ["rock", "paper", "scissor"]
 
b = random.choice(choices)

if a == "rock":
    print("You chose rock.")
    print("Computer chose", b)
    if b == "scissor":
        print("You win!")
    elif b == "paper":
        print("Computer wins!")
    else:
        print("It's a tie!")
if a == "paper":
    print("You chose paper.")
    print("Computer chose", b)
    if b == "rock":
        print("You win!")
    elif b == "scissor":
        print("Computer wins!")
    else:
        print("It's a tie!")
if a == "scissor":
    print("You chose scissor.")
    print("Computer chose", b)
    if b == "paper":
        print("You win!")
    elif b == "rock":
        print("Computer wins!")
    else:
        print("It's a tie!")   