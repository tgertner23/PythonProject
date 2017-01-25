import random
import craps
from matplotlib import pyplot as plt

#Setting the parameters
Nights=1000
roulette_tables=10
craps_tables=10
barmen=4
bartender_wage = 200
casinostartcash=50000
ncust=100
pctreturn=0.5
pctbach=0.1
pctnew=0.4
freebudget=200


#defining the class of customer
class Customer(object):
    def __init__(self, name):
        self.name = name

    def description(self):
        print(self.name)

#defining the property for returning customers
class Returner(Customer):
    @property
    #assignchips determines the number of chips for the player
    def assignchips(self):
        chips = random.randint(100, 300)
        return(chips)

# new customers
class New(Customer):
    @property
    def assignchips(self):
        chips = random.randint(200,300)
        return(chips)

# bachelors. they also receive the free budget
class Bachelor(Customer):
    @property
    def assignchips(self):
        chips = random.randint(200,500)+freebudget
        return(chips)
# Creates a list of players with the number of players set earlier
def CreatePlayers(nplayers):
    playerlist=[]
    for i in range(0,nplayers):
        playerlist.append("Player"+str(i+1))
    return(playerlist)
#Taking the list of players and determining their type. Type determined by the percentages of each type
def PlayerType(listofplayers):
    rnumb=pctreturn*100
    bnumb=pctbach*100
    ptype = []
    # generates a random number for each player that is the basis for the type
    #creates a list of types (R,B,or N). Also alters the input to have class involved
    for i in range(0, len(listofplayers)):
        rando=random.randint(1,100)

        if rando<rnumb:
            listofplayers[i]=Returner(str(listofplayers[i]))
            ptype.append("R")
        elif rando>(100-bnumb):
            listofplayers[i] = Bachelor(str(listofplayers[i]))
            ptype.append("B")
        else:
            listofplayers[i] = New(str(listofplayers[i]))
            ptype.append("N")
    return(ptype)
#Takes a list of players that have a class assigned and assigns the number of chips to the player
#returns a list
def PlayerChips(listofplayers):
    cashcash=[]
    for i in range(0,len(listofplayers)):
        cashcash.append(listofplayers[i].assignchips)
    return(cashcash)
#Roulette minimum bets list
RMinchoices=[50,100,200]
#Craps minimum bets list
CMinchoices=[0,25,50]

#Selects a table based on the number of tables for each game and the choice of the players
def ChooseATable(roulettetables,crapstables,actions):
    choiceoftables=[]
    for i in range(0,len(actions)):
        if actions[i]=="Roulette":
            choiceoftables.append(random.randint(1,roulettetables))
        elif actions[i]=="Craps":
            choiceoftables.append(random.randint(1,crapstables))
        else:
            choiceoftables.append(0)
    return(choiceoftables)

#The main function using inputs of number of nights, the number of players, the casino starting cash,
# the number of bartenders, & the number of craps and roulette tables.
def CasinoSimulation(nights, pnumber,casinoday1cash,nbartend,nroulette,ncraps):
    #setting the variable for the number of tips earned that can be used later for a bonus question
    global totaltips
    totaltips=0
    #determines the number of dealers (1 per table)
    nemployees=nroulette+ncraps
    #variable for the amount of money lost by the casino due to player winnings
    endlossfromp=0
    #setting the casino cash as the starting cash
    casinocash=casinoday1cash
    #list that will have the daily cash of the casino
    casinocashvector=[]
    #for a bonus. will find the profit from craps. the roulette one is the profit for roulette
    global crapsprofit
    crapsprofit=0
    global rouletteprofit
    rouletteprofit=0
    #for a bonus, the number of drinks purchased
    global purchaseddrinks
    purchaseddrinks=0
    #run a loop based on the number of nights
    for i in range(0,nights):
        #new list of player for each night
        plist=CreatePlayers(pnumber)
        #determines the types for each new player
        playertypes=PlayerType(plist)
        #how many bachelors are there?
        numbachelors=playertypes.count("B")
        #casino loses the free budget for each bachelor
        casinocash -= (freebudget*numbachelors)
        #determines player money
        PlayerMoney = PlayerChips(plist)
        #total player money for the night at the start
        #actions (or games) played per night.
        actionspernight = 40
        #the choice a player makes at each action can be sitting out a game
        choice = ["Roulette", "Craps", "Neither"]
        #drink orders are the number of drinks actually ordered
        #drink numbers are the number of drinks that the player should purchase in the night
        drinksorders=[]
        drinknumbers=[]
        for i in range(0,len(plist)):
            drinksorders.append(0)
            drinknumbers.append(random.randint(1,2))
        #run a loop for each action (or round)
        for i in range(0,actionspernight):
            #for each player, in round 1, they purchase a drink. tip is randomly determined. cost is 20
            for i in range(0,len(plist)):
                if drinksorders[i]==0:
                    tip = random.randint(0,20)
                    totaltips += tip
                    drinkcost = tip+20
                    PlayerMoney[i] -= drinkcost
                    drinksorders[i] += 1
                    purchaseddrinks +=1
                #if they do get 2 drinks, and they have money above 60, another drink is purchased
                elif drinksorders[i]==1 and drinknumbers[i]==2 and PlayerMoney[i]>60:
                    tip = random.randint(0, 20)
                    totaltips += tip
                    drinkcost = tip + 20
                    PlayerMoney[i] -= drinkcost
                    drinksorders[i] += 1
                    purchaseddrinks += 1
                # otherwise, they do not buy another drink
                else:
                    drinksorders[i] +=0
            #determines the current action for each player from the previous list of choices
            currentaction = [random.choice(choice) for i in range (0,len(plist))]
            #which table the player goes to.
            tablechoice=ChooseATable(nroulette,ncraps,currentaction)

            #this rounds min bet for Roulette
            Rminbet = random.choice(RMinchoices)
            #randomly determining the roulette wager
            rwager=[]
            for i in range (0, len(plist)):
                #if the player is not playing roulette, the player bets 0
                if currentaction[i] != "Roulette":
                    rwager.append(0)
                #returning players bet their money if they have less than the min bet
                elif playertypes[i]=="R":
                    if PlayerMoney[i]<Rminbet:
                        rwager.append(PlayerMoney[i])
                    else:
                        #returning players bet the min bet otherwise
                        rwager.append(Rminbet)
                #new players bet anywhere between zero to one third of their budget
                elif playertypes[i]=="N":
                    Rnewbwagerpct = random.uniform(0,(1/3))
                    rwager.append(int(PlayerMoney[i]*Rnewbwagerpct))
                #this is for bachelors. They bet anything between 0 and their total budget
                else:
                    rwager.append(int(random.uniform(0, PlayerMoney[i])))
            #now the min bet for craps
            Cminbet=random.choice(CMinchoices)
            #the wager for craps
            cwager=[]
            #same thing as above for craps instead of roulette
            for i in range(0,len(plist)):
                if currentaction[i] != "Craps":
                    cwager.append(0)
                elif playertypes[i] == "R":
                    if PlayerMoney[i] < Cminbet:
                        cwager.append(PlayerMoney[i])
                    else:
                        cwager.append(Cminbet)
                elif playertypes[i] == "N":
                    Cnewbwagerpct = random.uniform(0, (1 / 3))
                    cwager.append(int(PlayerMoney[i] * Cnewbwagerpct))
                else:
                    cwager.append(int(random.uniform(0, PlayerMoney[i])))
            #what the players choose as their guesses (r for roulette, c for craps)
            rguess=[]
            cguess=[]
            for i in range(0,len(plist)):
                #if the player sits out a round, he guesses out of range so he cannot win obviously
                if currentaction[i]=="Neither":
                    rguess.append(37)
                    cguess.append(1)
                #Roulette guesses are between 0 and 36. craps guess is out of range since you can't play both
                elif currentaction[i]=="Roulette":
                    rguess.append(random.randint(0,36))
                    cguess.append(1)
                #for craps, they can't bet on roulette so the guess is automatically wrong
                #the guess is between 2-12
                else:
                    rguess.append(37)
                    cguess.append(random.randint(2,12))
            #For each table, we randomly generate the correct number for roulette
            Rcorrectnumber=[]
            for i in range(0,roulette_tables):
                Rcorrectnumber.append(random.randint(0,36))
            #Money changes from roulette
            Rplayermoneychanges = []
            Rcasinomoneychanges = []
            #for each player
            for i in range(0, len(rguess)):
                #if the guess is correct for the specific table chosen and the bet is valid
                if rguess[i] == Rcorrectnumber[tablechoice[i]-1] and rwager[i] >= Rminbet:
                    #player wins 30 times his wager
                    Rplayermoneychanges.append(30 * rwager[i])
                    #casino therefore pays out the amount bet
                    Rcasinomoneychanges.append(-(30*rwager[i]))
                else:
                    #this is if the player didn't play roulette, bet below the min, or just guessed the wrong number
                    #players lose their bets while the casino earns the bet
                    Rplayermoneychanges.append(-rwager[i])
                    Rcasinomoneychanges.append(rwager[i])
            #The amount of chips won by the casino (not including losses)
            CasinoRouletteEarn=sum(Rcasinomoneychanges)
            #the profit from roulette is the revenue(from wrong or invalid bets) minus the amount players win
            rouletteprofit += CasinoRouletteEarn
            #same thing for craps now with the correct number list
            Ccorrectnumber=[]
            #generates the number by picking two random numbers between 1 and 6 that are summed
            for i in range(0,craps_tables):
                dicerolled=random.randint(1,6)+random.randint(1,6)
                Ccorrectnumber.append(dicerolled)
            #The money changes for craps, which works the same way as the roulette money changes did
            Cplayermoneychanges = []
            Ccasinomoneychanges = []
            for i in range(0,len(cguess)):
                if cguess[i] == Ccorrectnumber[tablechoice[i]-1] and cwager[i] >= Cminbet:
                    Cplayermoneychanges.append(craps.payouts(Ccorrectnumber[tablechoice[i]-1])*cwager[i])
                    Ccasinomoneychanges.append(-craps.payouts(Ccorrectnumber[tablechoice[i]-1])*cwager[i])
                else:
                    Cplayermoneychanges.append(-cwager[i])
                    Ccasinomoneychanges.append(cwager[i])
            #sum of the profit from each player
            CasinoCrapsEarn=sum(Ccasinomoneychanges)
            #this goes toward the total profit from craps
            crapsprofit += CasinoCrapsEarn
            #The total casino changes is the craps and roulette revenue
            TCasinoNightChange = CasinoRouletteEarn+CasinoCrapsEarn
            #the cash from this round is added to the casino stash
            casinocash += TCasinoNightChange
            #players earn their money now to be used in future rounds
            for i in range(0,len(plist)):
                PlayerMoney[i] += Rplayermoneychanges[i]
                PlayerMoney[i] += Cplayermoneychanges[i]
        #the bartenders are paid $200. the cost of the bartenders is the nightly wage times the number of bartenders

        costofbartenders=200* nbartend
        #this cost is daily
        casinocash -= costofbartenders
        #this list shows the cash flows over the days. It will be useful to see a graph of the results
        casinocashvector.append(casinocash)
    #after our loop for the nights, we can do our finish calculations
    casinocashprofit = casinocash-casinoday1cash
    #dealers or employees(not bartenders) get 0.5% of profit.
    #casino loses 0.5% of profit times the number of dealers
    employeeearnings = 0.005*casinocashprofit*nemployees
    casinocashprofit -= employeeearnings
    #returns the casino cash list but the global variables can still be printed later
    return(casinocashvector)

#runs the simulation based on set parameters and then plots the profits over time
Q4sim = CasinoSimulation(Nights,ncust,casinostartcash,barmen,roulette_tables,craps_tables)
x_series = [i for i in range(0,Nights)]
plt.plot(x_series,Q4sim)
plt.show()
#for the bonuses
#the amount of tips earn by the 4 bartenders over the nights
print(totaltips)

#the profits from the craps tables
print(crapsprofit)
#the profits from the roulette tables
print(rouletteprofit)

#roulette makes a higher profit (due to the lower payoff given the probabilities)