import random
from random import randint
random.seed(3456)

def AboveMinimum(dollas):
    boollist = []
    minimumbets = 90
    for i in range(0,len(dollas)):

        if (dollas[i]>minimumbets):
            boollist.append(True)
        else:
            boollist.append(False)
    return(boollist)

def SpinTheWheel(bets,okbet,dollas):
    newbets=[]
    for i in range(0, len(okbet)):
        if (okbet[i]==True):
            newbets.append(bets[i])
        else:
            newbets.append(37)
    landing=randint(0,36)
    print("Spinning the wheel...")
    print("Ball lands on "+str(landing))
    numwinners=newbets.count(landing)
    if (numwinners==0):
        playerwinnings = []
        print("There are no winners")
        casinowinnings=sum(dollas)
        for i in range(0,len(dollas)):
            playerwinnings.append(0)
        winningsoverall=[casinowinnings,playerwinnings]
        print(winningsoverall)
    else:
        print(str(numwinners) +" bet(s) got it this round.")
        playerwinnings = []
        casinopwinnings = []
        for i in range(0, len(dollas)):
            if (newbets[i]==landing and okbet[i]==True):
                playerwinnings.append(30*dollas[i])
                casinopwinnings.append(0)
            else:
                playerwinnings.append(0)
                casinopwinnings.append(dollas[i])
        casinowinnings=sum(casinopwinnings)
        winningsoverall=[casinowinnings,playerwinnings]
        print(winningsoverall)

def SimulateGame(numbers,money):
    Checking=[]
    Checking=AboveMinimum(money)
    SpinTheWheel(numbers,Checking,money)

