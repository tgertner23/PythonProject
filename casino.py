import random
import craps


#Defining the class of customer
class Customer(object):
    def __init__(self, name):
        self.name = name

    def description(self):
        print(self.name)

#Defining the property for returning customers
class Returner(Customer):
    @property
    #Assignchips determines the number of chips for the player
    def assignchips(self):
        chips = random.randint(100, 300)
        return(chips)

#New customers
class New(Customer):
    @property
    def assignchips(self):
        chips = random.randint(200, 300)
        return(chips)

#Bachelors. They also receive the free budget
class Bachelor(Customer):
    @property
    def assignchips(self):
        chips = random.randint(200,500)
        return(chips)
#Creates a list of players with the number of players set earlier
def CreatePlayers(nplayers):
    playerlist = []
    for i in range(0, nplayers):
        playerlist.append("Player" + str(i + 1))
    return(playerlist)
#Taking the list of players and determining their type. Type determined by the percentages of each type
def PlayerType(listofplayers, probreturn, probbach):
    rnumb = probreturn*100
    bnumb = probbach*100
    ptype = []
    #Generates a random number for each player that is the basis for the type
    #Creates a list of types (R,B,or N). Also alters the input to have class involved
    for i in range(0, len(listofplayers)):
        rando = random.randint(1,100)

        if rando <= rnumb:
            listofplayers[i] = Returner(str(listofplayers[i]))
            ptype.append("R")
        elif rando > (100-bnumb):
            listofplayers[i] = Bachelor(str(listofplayers[i]))
            ptype.append("B")
        else:
            listofplayers[i] = New(str(listofplayers[i]))
            ptype.append("N")
    return(ptype)
#Takes a list of players that have a class assigned and assigns the number of chips to the player
#Returns a list
def PlayerChips(listofplayers, typesofplayers, bachelorbudget):
    cashcash = []
    for i in range(0,len(listofplayers)):
        if typesofplayers[i]=="B":
            cashcash.append(listofplayers[i].assignchips+bachelorbudget)
        else:
            cashcash.append(listofplayers[i].assignchips)
    return(cashcash)
#Roulette minimum bets list
RMinchoices = [50,100,200]
#Craps minimum bets list
CMinchoices = [0,25,50]

#Selects a table based on the number of tables for each game and the choice of the players
def ChooseATable(roulettetables, crapstables, actions):
    choiceoftables = []
    for i in range(0, len(actions)):
        if actions[i]=="Roulette":
            choiceoftables.append(random.randint(1, roulettetables))
        elif actions[i]=="Craps":
            choiceoftables.append(random.randint(1, crapstables))
        else:
            choiceoftables.append(0)
    return(choiceoftables)

#The main function using inputs of number of nights, the number of players, the casino starting cash,
#the number of bartenders, & the number of craps and roulette tables.
def CasinoSimulation(nights, pnumber, casinoday1cash, nbartend, nroulette, ncraps, freebachelorbudget, pctr, pctb):
    #Setting the variable for the number of tips earned that can be used later for a bonus question
    global totaltips
    totaltips = 0
    #Determines the number of dealers (1 per table)
    nemployees = nroulette + ncraps
    #Setting the casino cash as the starting cash
    casinocash = casinoday1cash
    #List that will have the daily cash of the casino
    casinocashvector = []
    #For a bonus. Will find the profit from craps. The roulette one is the profit for roulette
    global crapsprofit
    crapsprofit = 0
    global rouletteprofit
    rouletteprofit = 0
    #For a bonus, the number of drinks purchased
    global purchaseddrinks
    purchaseddrinks = 0
    #Run a loop based on the number of nights
    for i in range(0, nights):
        #New list of player for each night
        plist = CreatePlayers(pnumber)
        #Determines the types for each new player
        playertypes = PlayerType(plist, pctr, pctb)
        #How many bachelors are there?
        numbachelors = playertypes.count("B")
        #Casino loses the free budget for each bachelor
        casinocash -= (freebachelorbudget*numbachelors)
        #Determines player money
        PlayerMoney = PlayerChips(plist, playertypes, freebachelorbudget)
        #Total player money for the night at the start
        #Actions (or games) played per night.
        actionspernight = 20
        #The choice a player makes at each action can be sitting out a game
        choice = ["Roulette", "Craps", "Neither"]
        #This will help make sure that the customers purchase drinks around five times
        roundsbetweendrinks = actionspernight/5
        #Loop run each round determining if the customer orders drinks or not
        for i in range(0,len(plist)):
            #In this case, it is between 1 and 4
            drinkornot = random.randint(1,roundsbetweendrinks)
            #There is a 25% chance that the player purchases a drink so if the random number is four, they will order
            if drinkornot==4 and PlayerMoney[i] > 60:
                #The player orders one or two drinks
                numofdrinks = random.randint(1,2)
                purchaseddrinks += numofdrinks
                #The tip is anything from zero to twenty
                tip = random.randint(0,20)
                #The cost of the drink without the tip is twenty times the number of drinks
                drinkcost = 20*numofdrinks
                #Casino gets the cost of the drink but not the tip
                casinocash += drinkcost
                #The player pays the cost of the drinks and the tip
                PlayerMoney[i] -= drinkcost
                PlayerMoney[i] -= tip
                totaltips += tip
            else:
                #In the other case, nothing happens
                purchaseddrinks += 0

            #Determines the current action for each player from the previous list of choices
            currentaction = [random.choice(choice) for i in range (0, len(plist))]
            #Which table the player goes to
            tablechoice = ChooseATable(nroulette, ncraps, currentaction)

            #This rounds min bet for Roulette
            Rminbet = random.choice(RMinchoices)
            #Randomly determining the roulette wager
            rwager = []
            for i in range (0, len(plist)):
                #If the player is not playing roulette, the player bets 0
                if currentaction[i] != "Roulette":
                    rwager.append(0)
                #Returning players bet their money if they have less than the min bet
                elif playertypes[i]=="R":
                    if PlayerMoney[i] < Rminbet:
                        rwager.append(PlayerMoney[i])
                    else:
                        #Returning players bet the min bet otherwise
                        rwager.append(Rminbet)
                #New players bet anywhere between zero to one third of their budget
                elif playertypes[i]=="N":
                    Rnewbwagerpct = random.uniform(0,(1/3))
                    rwager.append(int(PlayerMoney[i]*Rnewbwagerpct))
                #This is for bachelors. They bet anything between 0 and their total budget
                else:
                    rwager.append(int(random.uniform(0, PlayerMoney[i])))
            #Now the min bet for craps
            Cminbet = random.choice(CMinchoices)
            #The wager for craps
            cwager = []
            #Same thing as above for craps instead of roulette
            for i in range(0,len(plist)):
                if currentaction[i] != "Craps":
                    cwager.append(0)
                elif playertypes[i]=="R":
                    if PlayerMoney[i] < Cminbet:
                        cwager.append(PlayerMoney[i])
                    else:
                        cwager.append(Cminbet)
                elif playertypes[i]=="N":
                    Cnewbwagerpct = random.uniform(0, (1 / 3))
                    cwager.append(int(PlayerMoney[i]*Cnewbwagerpct))
                else:
                    cwager.append(int(random.uniform(0, PlayerMoney[i])))
            #What the players choose as their guesses (r for roulette, c for craps)
            rguess = []
            cguess = []
            for i in range(0,len(plist)):
                #If the player sits out a round, he guesses out of range so he cannot win obviously
                if currentaction[i]=="Neither":
                    rguess.append(37)
                    cguess.append(1)
                #Roulette guesses are between 0 and 36. Craps guess is out of range since you can't play both
                elif currentaction[i]=="Roulette":
                    rguess.append(random.randint(0,36))
                    cguess.append(1)
                #For craps, they can't bet on roulette so the guess is automatically wrong
                #The guess is between 2-12
                else:
                    rguess.append(37)
                    cguess.append(random.randint(2,12))
            #For each table, we randomly generate the correct number for roulette
            Rcorrectnumber = []
            for i in range(0,nroulette):
                Rcorrectnumber.append(random.randint(0,36))
            #Money changes from roulette
            Rplayermoneychanges = []
            Rcasinomoneychanges = []
            #For each player
            for i in range(0, len(rguess)):
                #If the guess is correct for the specific table chosen and the bet is valid
                if rguess[i] == Rcorrectnumber[tablechoice[i]-1] and rwager[i] >= Rminbet:
                    #Player wins 30 times his wager
                    Rplayermoneychanges.append(30*rwager[i])
                    #Casino therefore pays out the amount bet
                    Rcasinomoneychanges.append(-(30*rwager[i]))
                else:
                    #This is if the player didn't play roulette, bet below the min, or just guessed the wrong number
                    #Players lose their bets while the casino earns the bet
                    Rplayermoneychanges.append(-rwager[i])
                    Rcasinomoneychanges.append(rwager[i])
            #The amount of chips won by the casino (not including losses)
            CasinoRouletteEarn = sum(Rcasinomoneychanges)
            #The profit from roulette is the revenue(from wrong or invalid bets) minus the amount players win
            rouletteprofit += CasinoRouletteEarn
            #Same thing for craps now with the correct number list
            Ccorrectnumber = []
            #Generates the number by picking two random numbers between 1 and 6 that are summed
            for i in range(0,ncraps):
                dicerolled = random.randint(1,6) + random.randint(1,6)
                Ccorrectnumber.append(dicerolled)
            #The money changes for craps, which works the same way as the roulette money changes did
            Cplayermoneychanges = []
            Ccasinomoneychanges = []
            for i in range(0, len(cguess)):
                if cguess[i] == Ccorrectnumber[tablechoice[i]-1] and cwager[i] >= Cminbet:
                    Cplayermoneychanges.append(craps.payouts(Ccorrectnumber[tablechoice[i]-1])*cwager[i])
                    Ccasinomoneychanges.append(-craps.payouts(Ccorrectnumber[tablechoice[i]-1])*cwager[i])
                else:
                    Cplayermoneychanges.append(-cwager[i])
                    Ccasinomoneychanges.append(cwager[i])
            #Sum of the profit from each player
            CasinoCrapsEarn = sum(Ccasinomoneychanges)
            #This goes toward the total profit from craps
            crapsprofit += CasinoCrapsEarn
            #The total casino changes is the craps and roulette revenue
            TCasinoNightChange = CasinoRouletteEarn+CasinoCrapsEarn
            #The cash from this round is added to the casino stash
            casinocash += TCasinoNightChange
            #Players earn their money now to be used in future rounds
            for i in range(0,len(plist)):
                PlayerMoney[i] += Rplayermoneychanges[i]
                PlayerMoney[i] += Cplayermoneychanges[i]
        #The bartenders are paid $200. the cost of the bartenders is the nightly wage times the number of bartenders
        costofbartenders = 200*nbartend
        #This cost is daily
        casinocash -= costofbartenders
        #This list shows the cash flows over the days. It will be useful to see a graph of the results
        casinocashvector.append(casinocash)
    #After our loop for the nights, we can do our finish calculations
    casinocashprofit = casinocash - casinoday1cash
    #Dealers or employees(not bartenders) get 0.5% of profit.
    #Casino loses 0.5% of profit times the number of dealers
    employeeearnings = 0.005*casinocashprofit*nemployees
    casinocashprofit -= employeeearnings
    #Returns the casino cash list but the global variables can still be printed later
    return(casinocashvector)

#For the bonuses
#The amount of tips earn by the 4 bartenders over the nights
def bartendertips(nights, customers, cashstart, bartenders, rtables, ctables, freebachelorbudget, pctr, pctb):
    CasinoSimulation(nights, customers, cashstart, bartenders, rtables, ctables, freebachelorbudget, pctr, pctb)
    return(totaltips)

#The profits from the craps tables
def gameprofits(nights, customers, cashstart, bartenders, rtables, ctables, freebachelorbudget, pctr, pctb):
    CasinoSimulation(nights, customers, cashstart, bartenders, rtables, ctables, freebachelorbudget, pctr, pctb)
    print("The first number is the roulette profit. The second is the craps profit.")
    return([rouletteprofit, crapsprofit])