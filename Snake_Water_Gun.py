# Snake Water Game

import random


def gameWin(you, comp):
    # Condition for Game tie
    if(comp == you):
        return None

    # Checks all possibilities if computer choose Snake

    elif(comp == 's'):
        if(you == 'w'):
            return False
        elif(you == 'g'):
            return True

    # Checks all possibilities if computer choose Water

    elif(comp == 'w'):
        if(you == 'g'):
            return False
        elif(you == 's'):
            return True

    # Checks all possibilities if computer choose Gun

    elif(comp == 'g'):
        if(you == 's'):
            return False
        elif(you == 'w'):
            return True


# Random number generate from 1 to 30
num = random.randint(1, 30)
comp = print("Computer's turn")
you = input("Your's Turn: Enter 's' for Snake 'w' for Water and 'g' for Gun\n")
if(num <= 10):
    comp = 's'
elif(num > 10 and num <= 20):
    comp = 'w'
elif(num > 20 and num <= 30):
    comp = 'g'

# Function Call
result = gameWin(you, comp)

print(f"Computer choose {comp} and You choose {you}")

if(result == None):
    print("Game Tied!")
elif(result == True):
    print("Congratulations! You Win")
else:
    print("You Lose! Try again")
