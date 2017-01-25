import random
random.seed(3456)
#boolian check on the wager. if above the min, output is True. if below, output is False
def AboveMinimum(dollas):
    boollist = []
    minimumbets = 90
    for i in range(0,len(dollas)):

        if (dollas[i]>minimumbets):
            boollist.append(True)
        else:
            boollist.append(False)
    return(boollist)

#Main function
def SpinTheWheel(bets,dollas):
    #determines the random number the ball lands on
    landing=random.randint(0,36)
    #Dealer tells us what's happening and where the ball lands
    print("Spinning the wheel...")
    print("Ball lands on "+str(landing))
    #count of how many people were correct
    numwinners=bets.count(landing)
    #in the case of no winners
    if (numwinners==0):
        playerwinnings = []
        #the dealer fills the players hearts with shame
        print("There are no winners")
        #casino wins the wagers
        casinowinnings=sum(dollas)
        #player winnings will be a list of zeroes
        for i in range(0,len(dollas)):
            playerwinnings.append(0)
        #output
        winningsoverall=[casinowinnings,playerwinnings]
        print(winningsoverall)
    #if some lucky guy wins
    else:
        #We find our how many were correct
        print(str(numwinners) +" bet(s) got it this round.")
        playerwinnings = []
        casinopwinnings = []
        #loop for all players
        for i in range(0, len(dollas)):
            #if they are correct in their guess
            if (bets[i]==landing):
                #they win 30 times the wager while the casino wins nothing
                playerwinnings.append(30*dollas[i])
                casinopwinnings.append(0)
            else:
                #if they are wrong, the casino wins their wager and they get nothing
                playerwinnings.append(0)
                casinopwinnings.append(dollas[i])
        #casino winnings is the total of their list
        casinowinnings=sum(casinopwinnings)
        #output
        winningsoverall=[casinowinnings,playerwinnings]
        print(winningsoverall)

#final function
def SimulateGame(numbers,money):
    #running the boolian check
    Checking=AboveMinimum(money)
    #creating new bets so that the wagers below the min are changed to a number outside the possible range
    #in this case, it is 37. this way, this money is lost and the players are not considered winners
    newbets=[]
    for i in range(0, len(money)):
        if (Checking[i]==True):
            newbets.append(numbers[i])
        else:
            newbets.append(37)
    #spinning the wheel
    SpinTheWheel(newbets,money)

