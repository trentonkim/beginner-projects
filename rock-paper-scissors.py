import random
import time

cpuScore = 0
playerScore = 0

cpuHand = random.randint(1,3)
#1 is rock, 2 is paper, 3 is scissors


print("What hand would you like to throw out? (rock, paper, scissors)")
playerHand = input()


if playerHand == "rock":
    playerHandNumber = 4
if playerHand == "paper":
    playerHandNumber = 5
if playerHand == "scissors":
    playerHandNumber = 6

if cpuHand == 1:
    if playerHandNumber == 4:
        print("Tie! Nobody gets a point.")
        print("The player's score is " + str(playerScore) + ".")
        print("The computer's score is " + str(cpuScore) + ".")
    if playerHandNumber == 5:
        print("Player wins! Player gets one point.")
        playerScore +=1
        print("The player's score is " + str(playerScore) + ".")
        print("The computer's score is " + str(cpuScore) + ".")
    if playerHandNumber == 6:
        print("Player loses! Computer gets one point.")
        cpuScore +=1
        print("The player's score is " + str(playerScore) + ".")
        print("The computer's score is " + str(cpuScore) + ".")
if cpuHand == 2:
    if playerHandNumber == 4:
        print("Player loses! Computer gets one point.")
        cpuScore += 1
        print("The player's score is " + str(playerScore) + ".")
        print("The computer's score is " + str(cpuScore) + ".")
    if playerHandNumber == 5:
        print("Tie! Nobody gets a point.")
        print("The player's score is " + str(playerScore) + ".")
        print("The computer's score is " + str(cpuScore) + ".")
    if playerHandNumber == 6:
        print("Player wins! Player gets one point.")
        playerScore +=1
        print("The player's score is " + str(playerScore) + ".")
        print("The computer's score is " + str(cpuScore) + ".")
if cpuHand == 3:
    if playerHandNumber == 4:
        print("Player wins! Player gets one point.")
        playerScore +=1
        print("The player's score is " + str(playerScore) + ".")
        print("The computer's score is " + str(cpuScore) + ".")
    if playerHandNumber == 5:
        print("Player loses! Computer gets one point.")
        cpuScore +=1
        print("The player's score is " + str(playerScore) + ".")
        print("The computer's score is " + str(cpuScore) + ".")
    if playerHandNumber == 6:
        print("Tie! Nobody gets a point.")
        print("The player's score is " + str(playerScore) + ".")
        print("The computer's score is " + str(cpuScore) + ".")

print("Would you like to play again? (y/n)")
playerAnswer = input()

while playerAnswer == "y":
    print("What hand would you like to throw out? (rock, paper, scissors)")
    playerHand = input()

    if playerHand == "rock":
        playerHandNumber = 4
    if playerHand == "paper":
        playerHandNumber = 5
    if playerHand == "scissors":
        playerHandNumber = 6

    if cpuHand == 1:
        if playerHandNumber == 4:
            print("Tie! Nobody gets a point.")
            print("The player's score is " + str(playerScore) + ".")
            print("The computer's score is " + str(cpuScore) + ".")
        if playerHandNumber == 5:
            print("Player wins! Player gets one point.")
            playerScore += 1
            print("The player's score is " + str(playerScore) + ".")
            print("The computer's score is " + str(cpuScore) + ".")
        if playerHandNumber == 6:
            print("Player loses! Computer gets one point.")
            cpuScore += 1
            print("The player's score is " + str(playerScore) + ".")
            print("The computer's score is " + str(cpuScore) + ".")
    if cpuHand == 2:
        if playerHandNumber == 4:
            print("Player loses! Computer gets one point.")
            cpuScore =+1
            print("The player's score is " + str(playerScore) + ".")
            print("The computer's score is " + str(cpuScore) + ".")
        if playerHandNumber == 5:
            print("Tie! Nobody gets a point.")
            print("The player's score is " + str(playerScore) + ".")
            print("The computer's score is " + str(cpuScore) + ".")
        if playerHandNumber == 6:
            print("Player wins! Player gets one point.")
            playerScore += 1
            print("The player's score is " + str(playerScore) + ".")
            print("The computer's score is " + str(cpuScore) + ".")
    if cpuHand == 3:
        if playerHandNumber == 4:
            print("Player wins! Player gets one point.")
            playerScore += 1
            print("The player's score is " + str(playerScore) + ".")
            print("The computer's score is " + str(cpuScore) + ".")
        if playerHandNumber == 5:
            print("Player loses! Computer gets one point.")
            cpuScore += 1
            print("The player's score is " + str(playerScore) + ".")
            print("The computer's score is " + str(cpuScore) + ".")
        if playerHandNumber == 6:
            print("Tie! Nobody gets a point.")
            print("The player's score is " + str(playerScore) + ".")
            print("The computer's score is " + str(cpuScore) + ".")

    print("Would you like to play again? (y/n)")
    playerAnswer = input()

if playerAnswer == "n":
    print("Good game! The program will now shut down.")
    time.sleep(2.75)
    quit()
