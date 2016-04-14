# iodoiodon (Rock Paper Scissors AI)
#Gavin Su
# http://gavin.su
# v0.1

import random

# Markov Array
#   R P S Last Turn
# R x x x
# P x x x
# S x x x
markovArray = [[1,1,1],[1,1,1],[1,1,1]]

def showChain():
    print("Rock {}\nPaper {}\nScissors {}".format(markovArray[0],markovArray[1],markovArray[2]))

def recordMove(playerHand, throw):
    global markovArray
            
    if playerHand == "Rock":
        if throw == 1:
            markovArray[0][0] += 1
        elif throw == 2:
            markovArray[0][1] += 1
        else:
            markovArray[0][2] += 1
    elif playerHand == "Paper":
        if throw == 1:
            markovArray[1][0] += 1
        elif throw == 2:
            markovArray[1][1] += 1
        else:
            markovArray[1][2] += 1
    else:
        if throw == 1:
            markovArray[2][0] += 1
        elif throw == 2:
            markovArray[2][1] += 1
        else:
            markovArray[2][2] += 1
            

def iodoiodon(playerHandsHistory):
    global markovArray
    
    # 1 = Rock
    # 2 = Paper
    # 3 = Scissors
    
    handsDict = {"Rock":1,"Paper":2,"Scissors":3}
    
    # Basic three throw patterns to use/look for
    # pattern1 = ["Rock","Paper","Scissors"]
    # pattern2 = ["Rock","Scissors","Paper"]
    # pattern3 = ["Rock","Paper","Paper"]
    # pattern4 = ["Rock","Rock","Rock"]
    # pattern5 = ["Paper","Scissors","Paper"]
    # pattern6 = ["Paper","Scissors","Scissors"]
    
    
    if len(playerHandsHistory) < 2:
        return random.randrange(1,4)
    else:
        if playerHandsHistory[-1] == "Rock":
            recordMove(playerHandsHistory[-2],1)
            
            rockNextTotal = markovArray[0][0] + markovArray[0][1] + markovArray[0][2]
            rockNextRock = markovArray[0][0] / rockNextTotal
            rockNextPaper = markovArray[0][1] / rockNextTotal
            rockNextScissors = markovArray[0][2] / rockNextTotal
            
            rockLimit = 1 - rockNextRock
            paperLimit = rockLimit - rockNextPaper
            
            rollNext = random.random()
            
            if rollNext >= rockLimit:
                return 2
            elif rollNext >= paperLimit:
                return 3
            else:
                return 1
        elif playerHandsHistory[-1] == "Paper":
            recordMove(playerHandsHistory[-2],2)
            
            paperNextTotal = markovArray[1][0] + markovArray[1][1] + markovArray[1][2]
            paperNextRock = markovArray[1][0] / paperNextTotal
            paperNextPaper = markovArray[1][1] / paperNextTotal
            paperNextScissors = markovArray[1][2] / paperNextTotal
            
            rockLimit = 1 - paperNextRock
            paperLimit = rockLimit - paperNextPaper
            
            rollNext = random.random()
            
            if rollNext >= rockLimit:
                return 2
            elif rollNext >= paperLimit:
                return 3
            else:
                return 1
        else:
            recordMove(playerHandsHistory[-2],3)
            
            scissorsNextTotal = markovArray[2][0] + markovArray[2][1] + markovArray[2][2]
            scissorsNextRock = markovArray[2][0] / scissorsNextTotal
            scissorsNextPaper = markovArray[2][1] / scissorsNextTotal
            scissorsNextScissors = markovArray[2][2] / scissorsNextTotal
            
            rockLimit = 1 - scissorsNextRock
            paperLimit = rockLimit - scissorsNextPaper
            
            rollNext = random.random()
            
            if rollNext >= rockLimit:
                return 2
            elif rollNext >= paperLimit:
                return 3
            else:
                return 1
        
