import random
from random import randint
random.seed(3456)

#this determines the payoffs and will be used to determine the winnings for the players
def payouts(roll):
    # the odds of rolling 2 or 12 is 1/36. the payoff is then $36 for every dollar bet IF 100% goes back to players
    if roll==2 or roll==12:
        pomult=36
    #for 3 and 11, the odds are 2/36 or 1/18. thus the payoff is $18 for every dollar
    elif roll==3 or roll==11:
        pomult=18
    #This continues the pattern, but odds are now 3/36
    elif roll==4 or roll==10:
        pomult=12
    #Odds are 4/36 now
    elif roll==5 or roll==9:
        pomult=9
    #Odds are 5/36
    elif roll==6 or roll==8:
        pomult=7.2
    #This is for the roll equaling 7 which has probability of 6/36
    else:
        pomult=6
    #Casino makes a 10% profit. So payoffs must be multiplied by 0.9 for the players getting 90% back.
    Casinowins=0.9*pomult
    #we will later multiply this by the wager of the winning players
    return(Casinowins)

#a function for the boolian check of meeting the minimum bet (set at 10 here)
def AboveMinimum(dollas):
    boollist = []
    minimumbets = 10
    #loop for each player
    for i in range(0,len(dollas)):
        #if the bet is above the min, it returns TRUE
        if (dollas[i]>minimumbets):
            boollist.append(True)
        #if not, it is an invalid bet and receives the FALSE response
        else:
            boollist.append(False)
    return(boollist)
#here we find out the correct number
def Dices():
    #to get the odds correct, we use two die instead of one.
    dice1=randint(1,6)
    dice2=randint(1,6)
    #the sum of these two numbers is the correct number
    rollbounce=dice1+dice2
    return(rollbounce)

#the main function
def RollTheDices(guesses,wagers):
    #prints the statement below
    print("Throwing the dice...")
    #determines the correct number
    theroll=Dices()
    #Stating the correct number
    print("We have " + str(theroll))
    #how many winners there are
    numwinners = guesses.count(theroll)
    #if there are 0 winners
    if (numwinners == 0):
        playerwinnings = []
        print("There are no winners")
        #casino wins the wagers
        casinowinnings = sum(wagers)
        #players earn nothing
        for i in range(0, len(wagers)):
            playerwinnings.append(0)
        #final output
        winningsoverall = [casinowinnings, playerwinnings]
        print(winningsoverall)
        return(winningsoverall)
    #if there is at least 1 winner
    else:
        #how many won
        print(str(numwinners) + " player(s) won!")
        playerwinnings = []
        casinopwinnings = []
        #for each bet
        for i in range(0, len(wagers)):
            #if they were correct, they get the payout based on the roll multiplied by the wager
            #the casino gets nothing there
            if (guesses[i] == theroll):
                playerwinnings.append(payouts(theroll) * wagers[i])
                casinopwinnings.append(0)
            #for those that lost
            else:
                #the players get nothing while the casino gets their wager
                playerwinnings.append(0)
                casinopwinnings.append(wagers[i])
        #casino is transformed from per player winnings to a total
        casinowinnings = sum(casinopwinnings)
        #final output
        winningsoverall = [casinowinnings, playerwinnings]
        print(winningsoverall)
        return(winningsoverall)
#final command
def SimulateGame(guesses,wagers):

    nguess = []
    #checks if the bets are ok
    okbet = AboveMinimum(wagers)
    #makes new guesses based on validity of bets.
    #if the bet is above the min, then the nguess (new guess) is the same as the old
    #if the bet is below the min, the guess is changed to 0 which is never a correct guess
    #this way, the invalid bets are never winners
    for i in range(0, len(okbet)):
        if (okbet[i] == True):
            nguess.append(guesses[i])
        else:
            nguess.append(0)
    #run the roll the dices based on the new guesses (nguess)
    out=RollTheDices(nguess,wagers)
    return(out)
