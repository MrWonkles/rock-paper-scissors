import random as ran
from time import sleep

##
## Custom functions designed to call one another in sequence
## or recurse as needed.
##
## Sleep function called to pace terminal output.
##

def playerStartCheck():

    playGame = input("Type Y or N: ")

    if playGame == "Y" or playGame == "y":
        print("\n")
        sleep(1)
        startMenu()
    elif playGame == "N" or playGame == "n":
        print("Goodbye!\n")
        sleep(1)
        exit()
    else:
        print("That's not a correct choice.\n")
        playerStartCheck()

def startMenu():

    print("------------------------------------------")
    print("  Beat 3 rounds and you win! Good luck!")
    print("------------------------------------------\n")
    playerChooses()

def playerChooses():
    print("1 -- Rock\n2 -- Paper\n3 -- Scissors\n")

    global playerChoice
    playerChoice = input("Choose... ")

    if playerChoice == '1' or playerChoice == '2' or playerChoice == '3':
        if playerChoice == '1': playerChoice = rpsChoices[0]
        if playerChoice == '2': playerChoice = rpsChoices[1]
        if playerChoice == '3': playerChoice = rpsChoices[2]
        print(f"You chose {playerChoice}.")
        compChooses()
    else:
        playerChooses()

def compChooses():
    global compChoice
    compChoice = ran.choice(rpsChoices)
    sleep(1)
    print(f"The computer chose {compChoice}.\n")
    sleep(1)
    roundEval()

def roundEval():
    ##
    ## Global variables declared to allow the function access
    ##
    
    global compScore
    global playerScore

    if playerChoice == rpsChoices[0]:
        if compChoice == rpsChoices[1]:
            print(f"{compChoice} beats {playerChoice}. You LOSE!")
            compScore += 1
        elif compChoice == rpsChoices[2]:
            print(f"{playerChoice} beats {compChoice}. You WIN!")
            playerScore += 1
        else: print("TIE!")  

    elif playerChoice == rpsChoices[1]:
        if compChoice == rpsChoices[2]:
            print(f"{compChoice} beats {playerChoice}. You LOSE!")
            compScore += 1
        elif compChoice == rpsChoices[0]:
            print(f"{playerChoice} beats {compChoice}. You WIN!")
            playerScore += 1
        else: print("TIE!") 

    elif playerChoice == rpsChoices[2]:
        if compChoice == rpsChoices[0]:
            print(f"{compChoice} beats {playerChoice}. You LOSE...")
            compScore += 1
        elif compChoice == rpsChoices[1]:
            print(f"{playerChoice} beats {compChoice}. You WIN!")
            playerScore += 1
        else: print("TIE!")

    sleep(1)
    print(f"\nYour score: {playerScore}\tComputer score: {compScore}\n")
    sleep(1)

    if playerScore >= 3:
        print("You win the game!\n")
    elif compScore >= 3:
        print("You lose the game...\n")
    else:
        playerChooses()

##
## Tuple used and referenced to maintain name choice integrity.
## Global variables used for score tracking and incrementation. 
##

rpsChoices = ('Rock', 'Paper', 'Scissors')
playerScore = 0
compScore = 0

print("\nWelcome to Rock, Paper, Scissors!\n")
sleep(1)
print("Do you want to play?")

playerStartCheck()


