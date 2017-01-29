import random
from random import randint
#This is used to fix the random generator so we can test the output
random.seed(3456)

#This determines the payoffs and will be used to determine the winnings for the players
#Scaling the payoffs based on probabilites so that the expected outcomes are the same across possible guesses
def payouts(roll):
    #The odds of rolling 2 or 12 is 1/36. the payoff is then $36 for every dollar bet IF 100% goes back to players
    if roll==2 or roll==12:
        pomult = 36
    #For 3 and 11, the odds are 2/36 or 1/18. Thus the payoff is $18 for every dollar
    elif roll==3 or roll==11:
        pomult = 18
    #This continues the pattern, but odds are now 3/36
    elif roll==4 or roll==10:
        pomult = 12
    #Odds are 4/36 now
    elif roll==5 or roll==9:
        pomult = 9
    #Odds are 5/36
    elif roll==6 or roll==8:
        pomult = 7.2
    #This is for the roll equaling 7 which has probability of 6/36
    else:
        pomult = 6
    #Casino makes a 10% profit. So payoffs must be multiplied by 0.9 for the players getting 90% back.
    Casinowins = 0.9*pomult
    #We will later multiply this by the wager of the winning players
    return(Casinowins)

#A function for the boolian check of meeting the minimum bet (set at 10 here)
def AboveMinimum(dollars):
    boollist = []
    #Arbitrarily chosen (no guideline given)
    minimumbets = 10
    #Loop for each player
    for i in range(0, len(dollars)):
        #If the bet is above the min, it returns TRUE
        if (dollars[i] >= minimumbets):
            boollist.append(True)
        #If not, it is an invalid bet and receives the FALSE response
        else:
            boollist.append(False)
    return(boollist)

#Here we find out what the sum of dice is
def Dices():
    #To get the odds correct, we use two die instead of one.
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    #The sum of these two numbers is the correct number
    rollbounce = dice1 + dice2
    return(rollbounce)

#The main function
def RollTheDices(guesses, wagers):
    #Prints the statement below
    print("Throwing the dice...")
    #Determines the sum of the dice
    theroll = Dices()
    #Stating the correct number
    print("We have " + str(theroll))
    #How many winners there are
    numwinners = guesses.count(theroll)
    #If there are no winners
    if (numwinners == 0):
        playerwinnings = []
        print("There are no winners")
        #Casino wins the wagers
        casinowinnings = sum(wagers)
        #Players earn nothing
        for i in range(0, len(wagers)):
            playerwinnings.append(0)
        #Final output
        winningsoverall = [casinowinnings, playerwinnings]
        print(winningsoverall)
        return(winningsoverall)
    #If there is at least one winner
    else:
        #How many won
        print(str(numwinners) + " player(s) won!")
        playerwinnings = []
        casinopwinnings = []
        #For each bet
        for i in range(0, len(wagers)):
            #If they were correct, they get the payout based on the roll multiplied by the wager
            #The casino gets nothing there
            if (guesses[i]==theroll):
                playerwinnings.append(payouts(theroll)*wagers[i])
                casinopwinnings.append(0)
            #For those that lost
            else:
                #The players get nothing while the casino gets their wager
                playerwinnings.append(0)
                casinopwinnings.append(wagers[i])
        #Casino is transformed from per player winnings to a total
        casinowinnings = sum(casinopwinnings)
        #Final output
        winningsoverall = [casinowinnings, playerwinnings]
        print(winningsoverall)
        return(winningsoverall)



#Final command
def SimulateGame(guesses, wagers):
    nguess = []
    #Checks if the bets are ok
    Checking = AboveMinimum(wagers)
    #Makes new guesses based on validity of bets.
    #If the bet is above the min, then the nguess (new guess) is the same as the old
    #If the bet is below the min, the guess is changed to 0 which is never a correct guess
    #This way, the invalid bets are never winners
    for i in range(0, len(Checking)):
        if (Checking[i]==True):
            nguess.append(guesses[i])
        else:
            nguess.append(0)
    #Run the roll the dices based on the new guesses (nguess)
    out=RollTheDices(nguess, wagers)
    return(out)

#Testing that casino makes 10% profit from payoffs
def ProfitTest():
    #Craps guesses
    crapguesses = [7, 9, 2, 11, 3]
    #The wagers for craps
    crapbets = [50, 70, 30, 40, 50]
    #Setting the player earnings to 0 and chips too
    playerearnings = 0
    chips = 0
    #Running the code 10000 times
    for i in range(0, 10000):
        #Chips is the sum of the wagers for each simulation
        chips += sum(crapbets)
        profittest=SimulateGame(crapguesses,crapbets)
        #The player earnings equals the sum of the earnings for each player
        playerearnings += sum(profittest[1])
    #This number should be close to 0.9
    print(playerearnings/chips)

