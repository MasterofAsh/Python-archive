# Snake Water Gun
# Exercise 5
"""
1. Snake-Water-Gun is a variation of Rock-Paper-Scissors, where players use hand gestures to represent
a snake, water, or a gun. The Gun beats the Snake, the Snake beats the water, and the water beats the Gun.
2. Write a python program to create a Snake-Water-Gun in python using if-else statements. Use proper
functions to check for win.
"""
import random

userChoice = None
userQuit = False
rounds = 0
startGame = None



def welcome():
    start = "Welcome to the game \' SNAKE-WATER-GUN \'"
    start = start.center(100)
    print(start)

def showMenu():
    choice = int(input("What would you like to do: \n" \
    "1. Read Rules \n" \
    "2. Play the game \n" \
    "3. Quit \n" \
    "Please select any ONE option with the corresponding number. \n"))
    return choice

def Rules():
    print("\nThese are the rules: \n1. Snake beats water \n2. Water beats Gun \n3. Gun beats Snake")

def game():
    print("This game is played with the computer. You can choose the amount of rounds you want to play:")
    playGame = input("Do you want to play the game? (Yes / No) \n")
    startGame = None

    if (playGame == "Yes"):
        roundChoice = int(input("1. 3 Rounds \n2. 4 Rounds \n3. 5 Rounds \n"
        "How many rounds do you want to play: \n"))
        startGame = True
        
        
        if (roundChoice == 1):
            rounds = 3
            print("\nThis game will be of Three rounds.")
            return rounds, startGame
        
    elif (playGame == "No"):
        print("Going back to the menu.")
        showMenu()
        startGame = False
        return startGame
        

def swgGame():

    activeRounds = 0
    print(rounds)
    finalResult = []

    while (activeRounds != rounds):
        actions = ["Snake", "Water", "Gun"]
        compAction = random.choice(actions)
        print(compAction)

        plrAction = input("What action do you want to perform?\n" \
        "Action (Snake / Water / Gun): ")
        
        match (plrAction, compAction):
            case ("Snake", "Snake"):
                print("\nComputer Action: ", compAction, "VS", "Your Action: ", plrAction)
                result = "Draw"
                print("Draw")
                finalResult.append(result)

            case ("Snake", "Water"):
                print("\nComputer Action: ", compAction, "VS", "Your Action: ", plrAction)
                result = "Win"
                print("Win")
                finalResult.append(result)

            case ("Water", "Snake"):
                print("\nComputer Action: ", compAction, "VS", "Your Action: ", plrAction)
                result = "Lose"
                print("Lose")
                finalResult.append(result)

            case ("Water", "Water"):
                print("\nComputer Action: ", compAction, "VS", "Your Action: ", plrAction)
                result = "Draw"
                print("Draw")
                finalResult.append(result)

            case ("Gun", "Water"):
                print("\nComputer Action: ", compAction, "VS", "Your Action: ", plrAction)
                result = "Lose"
                print("Lose")
                finalResult.append(result)

            case ("Water", "Gun"):
                print("\nComputer Action: ", compAction, "VS", "Your Action: ", plrAction)
                result = "Win"
                print("Win")
                finalResult.append(result)

            case ("Gun", "Gun"):
                print("\nComputer Action: ", compAction, "VS", "Your Action: ", plrAction)
                result = "Draw"
                print("Draw")
                finalResult.append(result)

            case ("Gun", "Snake"):
                print("\nComputer Action: ", compAction, "VS", "Your Action: ", plrAction)
                result = "Win"
                print("Win")
                finalResult.append(result)

            case ("Snake", "Gun"):
                print("\nComputer Action: ", compAction, "VS", "Your Action: ", plrAction)
                result = "Lose"
                print("Lose")
                finalResult.append(result)

        activeRounds = activeRounds + 1

    print(finalResult)
        


welcome()
# userChoice = showMenu()
# # while (userQuit == False):


while (userQuit == False):
    userChoice = showMenu()
    if (userChoice == 1):
        Rules()

    elif (userChoice == 2):
        rounds = game()
        
            

    elif (userChoice == 3):
        print("Quitting the menu.")
        userQuit = True
        
    else:
        print("Please enter a valid input.")
        print("Going back to the menu.\n")
        showMenu()
    

