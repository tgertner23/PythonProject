import random
#This is used to fix the random generator so we can test the output
random.seed(3456)

#Boolian check on the wager (amount of money bet).
#If above the min, output is True. If below, output is False
def AboveMinimum(dollars):
    boollist = []
    minimumbets = 90
    for i in range(0,len(dollars)):
        if (dollars[i] > minimumbets):
            boollist.append(True)
        else:
            boollist.append(False)
    return(boollist)

#Main function
def SpinTheWheel(guesses,dollars):
    #Determines the random number the ball lands on
    landing = random.randint(0, 36)
    #Dealer tells us what's happening and where the ball lands
    print("Spinning the wheel...")
    print("Ball lands on " + str(landing))
    #Count of how many people win
    numwinners = guesses.count(landing)

    #In the case of no winners
    if (numwinners==0):
        playerwinnings = []
        #The dealer states that no one has won
        print("There are no winners")
        #Casino wins all the wagers
        casinowinnings = sum(dollars)
        #Player winnings will be a list of zeroes
        for i in range(0, len(dollars)):
            playerwinnings.append(0)
        #Output
        winningsoverall = [casinowinnings, playerwinnings]
        print(winningsoverall)

    #In the other case (at least one winner)
    else:
        #We find our how many were correct
        print(str(numwinners) +" bet(s) got it this round.")
        playerwinnings = []
        casinopwinnings = []
        #Loop for all players
        for i in range(0, len(dollars)):
            #If they are correct in their guess
            if (guesses[i]==landing):
                #They win 30 times the wager while the casino wins nothing
                playerwinnings.append(30*dollars[i])
                casinopwinnings.append(0)
            else:
                #If they are wrong, the casino wins their wager and they get nothing
                playerwinnings.append(0)
                casinopwinnings.append(dollars[i])
        #Casino winnings is the total of their list
        casinowinnings = sum(casinopwinnings)
        #Output
        winningsoverall = [casinowinnings, playerwinnings]
        print(winningsoverall)

#Final function
def SimulateGame(numbers, money):
    #Running the boolian check
    Checking = AboveMinimum(money)
    #Creating new bets so that the wagers below the min are changed to a number outside the possible range
    #In this case, it is 37. This way, this money is lost and the players are not considered winners
    newguess = []
    for i in range(0, len(money)):
        if (Checking[i]==True):
            newguess.append(numbers[i])
        else:
            newguess.append(37)
    SpinTheWheel(newguess, money)

