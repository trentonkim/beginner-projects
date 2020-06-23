import random

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
    if playerHandNumber == 5:
        print("Player wins! Player gets one point.")
        playerScore +=1
    if playerHandNumber == 6:
        print("Player loses! Computer gets one point.")
        cpuScore +=1
if cpuHand == 2:
    if playerHandNumber == 4:
        print("Player loses! Computer gets one point.")
    if playerHandNumber == 5:
        cpuScore +=1
        print("Tie! Nobody gets a point.")
    if playerHandNumber == 6:
        print("Player wins! Player gets one point.")
        playerScore +=1
if cpuHand == 3:
    if playerHandNumber == 4:
        print("Player wins! Player gets one point.")
        playerScore +=1
    if playerHandNumber == 5:
        print("Player loses! Computer gets one point.")
        playerScore +=1
    if playerHandNumber == 6:
        print("Tie! Nobody gets a point.")