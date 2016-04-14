# iodoiodon (Rock Paper Scissors AI)
#Gavin Su
# http://gavin.su
# v0.1

import random

def iodoiodon(playerHandsHistory):
    
    # 1 = Rock
    # 2 = Paper
    # 3 = Scissors
    
    if len(playerHandsHistory) == 0:
        return 2
    else:
        return random.randrange(1,4)
