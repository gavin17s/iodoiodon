# Simple Rock Paper Scissors Program to interact with iodoiodon.
# Gavin Su
# http://gavin.su
# v0.1

from iodoiodon import *

def winner(cpuChoice, playerChoice):
	if cpuChoice == "Rock" and playerChoice == "Scissors":
		return 0
	elif cpuChoice == "Rock" and playerChoice == "Paper":
		return 1
	elif cpuChoice == "Paper" and playerChoice == "Rock":
		return 0
	elif cpuChoice == "Paper" and playerChoice == "Scissors":
		return 1
	elif cpuChoice == "Scissors" and playerChoice == "Rock":
		return 1
	elif cpuChoice == "Scissors" and playerChoice == "Paper":
		return 0
	else:
		return 2
        
def main():
    
    print("############################################################")
    print("Rock Paper Scissors v0.1 by Gavin Su, http://gavin.su")
    print("############################################################")
    
    while True:
        try:
            rounds = int(input("How many rounds would you like to play? ")) + 1
        except ValueError:
            print('Invalid input. Try again.')
            print("-------------------------------------------------------")
        else:
            break
            
    print("-------------------------------------------------------")

    currentRound = 1
    handsDict = {1:"Rock",2:"Paper",3:"Scissors"}
    playerHand = ""
    playerWins = 0

    cpuHand = 0
    cpuWins = 0
    draws = 0
    
    playerHandsHistory = []
    cpuHandsHistory = []

    whoWon = 0

    while currentRound != rounds:
        print("Round", currentRound)
        print("-------------------------------------------------------")
        
        cpuHand = handsDict[iodoiodon(playerHandsHistory)]
        cpuHandsHistory.append(cpuHand)
        print("The computer has chosen its hand, what would you like to pick?")
        
        while True:
            try:
                playerHand = handsDict[int(input(
                "Enter 1 for Rock, 2 for Paper, or 3 for Scissors. "))]
                print("-------------------------------------------------------")
            except KeyError:
                print('Invalid input. Try again.')
                print("-------------------------------------------------------")
            except ValueError:
                print('Invalid input. Try again.')
                print("-------------------------------------------------------")
            else:
                break
        
        print("...")
        
        playerHandsHistory.append(playerHand)
        whoWon = winner(cpuHand, playerHand)

        if whoWon == 0:
            print("You chose {} and the CPU chose {}.".format(playerHand, cpuHand))
            print("The CPU wins this round!")
            cpuWins += 1
        elif whoWon == 1:
            print("You chose {} and the CPU chose {}.".format(playerHand, cpuHand))
            print("You have won this round!")
            playerWins += 1
        else:
            print("You chose {} and the CPU also chose {}.".format(playerHand, cpuHand))
            print("You have tied this round!")
            draws += 1
            
        print("-------------------------------------------------------")

        currentRound += 1

    if cpuWins > playerWins:
        print("The CPU has won the game with {} win(s) out of {} Round(s).\nThere were {} draw(s)."
        .format(cpuWins, rounds - 1, draws))
    elif playerWins > cpuWins:
        print("You have won the game with {} win(s) out of {} Round(s).\nThere were {} draw(s)."
        .format(playerWins, rounds - 1, draws))
    else:
        print("The game has ended in a draw!")
        
    print("############################################################")
    print(cpuHandsHistory)
    print(playerHandsHistory)
    showChain()
        
if __name__ == '__main__':
    main()
