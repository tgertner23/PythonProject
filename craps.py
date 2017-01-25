import random
from random import randint
random.seed(3456)

def payouts(roll):
    if roll==2 or roll==12:
        pomult=36
    elif roll==3 or roll==11:
        pomult=18
    elif roll==4 or roll==10:
        pomult=12
    elif roll==5 or roll==9:
        pomult=9
    elif roll==6 or roll==8:
        pomult=7.2
    else:
        pomult=6
    Casinowins=0.9*pomult
    return(Casinowins)


def AboveMinimum(dollas):
    boollist = []
    minimumbets = 10
    for i in range(0,len(dollas)):

        if (dollas[i]>minimumbets):
            boollist.append(True)
        else:
            boollist.append(False)
    return(boollist)

def Dices():
    dice1=randint(1,6)
    dice2=randint(1,6)
    rollbounce=dice1+dice2
    return(rollbounce)

def RollTheDices(guesses,wagers):
    nguess = []
    okbet = AboveMinimum(wagers)

    for i in range(0, len(okbet)):
        if (okbet[i] == True):
            nguess.append(guesses[i])
        else:
            nguess.append(0)
    print("Throwing the dice...")
    theroll=Dices()
    print("We have " + str(theroll))
    numwinners = nguess.count(theroll)
    if (numwinners == 0):
        playerwinnings = []
        print("There are no winners")
        casinowinnings = sum(wagers)
        for i in range(0, len(wagers)):
            playerwinnings.append(0)
        winningsoverall = [casinowinnings, playerwinnings]
        print(winningsoverall)
        return(winningsoverall)
    else:
        print(str(numwinners) + " player(s) won!")
        playerwinnings = []
        casinopwinnings = []
        for i in range(0, len(wagers)):
            if (nguess[i] == theroll and okbet[i] == True):
                playerwinnings.append(payouts(theroll) * wagers[i])
                casinopwinnings.append(0)
            else:
                playerwinnings.append(0)
                casinopwinnings.append(wagers[i])
        casinowinnings = sum(casinopwinnings)
        winningsoverall = [casinowinnings, playerwinnings]
        print(winningsoverall)
        return(winningsoverall)

def SimulateGame(guesses,wagers):
    out=RollTheDices(guesses,wagers)
    return(out)
