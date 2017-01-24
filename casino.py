import random
import craps
from matplotlib import pyplot as plt
import numpy



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


class Customer(object):
    def __init__(self, name):
        self.name = name

    def description(self):
        print(self.name)

class Returner(Customer):
    @property
    def asschips(self):
        chips = random.randint(100, 300)
        return(chips)

class New(Customer):
    @property
    def asschips(self):
        chips = random.randint(200,300)
        return(chips)

class Bachelor(Customer):
    @property
    def asschips(self):
        chips = random.randint(200,500)+freebudget
        return(chips)

def CreatePlayers(nplayers):
    playerlist=[]
    for i in range(0,nplayers):
        playerlist.append("Player"+str(i+1))
    return(playerlist)
def PlayerType(listofplayers):
    rnumb=pctreturn*100
    bnumb=pctbach*100
    ptype = []
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
def PlayerChips(listofplayers):
    cashcash=[]
    for i in range(0,len(listofplayers)):
        cashcash.append(listofplayers[i].asschips)
    return(cashcash)

RMinchoices=[50,100,200]
CMinchoices=[0,25,50]



def CasinoSimulation(nights, pnumber,casinoday1cash,nbartend,nroulette,ncraps,returntype):
    totaltips=0
    nemployees=nroulette+ncraps
    endlossfromp=0
    casinocash=casinoday1cash
    casinocashvector=[]
    crapsprofit=0
    rouletteprofit=0
    purchaseddrinks=0
    for i in range(0,nights):
        plist=CreatePlayers(pnumber)
        playertypes=PlayerType(plist)
        numbachelors=playertypes.count("B")
        casinocash -= (freebudget*numbachelors)
        PlayerMoney = PlayerChips(plist)
        Playerchipsamount=sum(PlayerMoney)
        actionspernight = 25
        choice = ["Roulette", "Craps", "Neither"]
        drinksorders=[]
        drinknumbers=[]
        for i in range(0,len(plist)):
            drinksorders.append(0)
            drinknumbers.append(random.randint(1,2))

        for i in range(0,actionspernight):
            for i in range(0,len(plist)):
                if drinksorders[i]==0:
                    tip = random.randint(0,20)
                    totaltips += tip
                    drinkcost = tip+20
                    PlayerMoney[i] -= drinkcost
                    drinksorders[i] += 1
                    purchaseddrinks +=1
                elif drinksorders[i]==1 and drinknumbers[i]==2 and PlayerMoney[i]>60:
                    tip = random.randint(0, 20)
                    totaltips += tip
                    drinkcost = tip + 20
                    PlayerMoney[i] -= drinkcost
                    drinksorders[i] += 1
                    purchaseddrinks += 1
                else:
                    drinksorders[i] +=0
            currentaction = [random.choice(choice) for i in range (0,len(plist))]
            tablechoice=[]
            for i in range(0,len(currentaction)):
                if currentaction[i]=="Roulette":
                    tablechoice.append(random.randint(1,roulette_tables))
                elif currentaction[i]=="Craps":
                    tablechoice.append(random.randint(1,craps_tables))
                else:
                    tablechoice.append(0)
            #roulette action
            Rminbet = random.choice(RMinchoices)
            rwager=[]
            for i in range (0, len(plist)):
                if currentaction[i] != "Roulette":
                    rwager.append(0)
                elif playertypes[i]=="R":
                    if PlayerMoney[i]<Rminbet:
                        rwager.append(PlayerMoney[i])
                    else:
                        rwager.append(Rminbet)
                elif playertypes[i]=="N":
                    Rnewbwagerpct = random.uniform(0,(1/3))
                    rwager.append(int(PlayerMoney[i]*Rnewbwagerpct))
                else:
                    rwager.append(int(random.uniform(0, PlayerMoney[i])))
            Cminbet=random.choice(CMinchoices)
            cwager=[]
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
            rguess=[]
            cguess=[]
            for i in range(0,len(plist)):
                if currentaction[i]=="Neither":
                    rguess.append(37)
                    cguess.append(1)
                elif currentaction[i]=="Roulette":
                    rguess.append(random.randint(0,36))
                    cguess.append(1)
                else:
                    rguess.append(37)
                    cguess.append(random.randint(2,12))
            Rcorrectnumber=[]
            for i in range(0,roulette_tables):
                Rcorrectnumber.append(random.randint(0,36))
            Rplayermoneychanges = []
            Rcasinomoneychanges = []
            for i in range(0, len(rguess)):
                if rguess[i] == Rcorrectnumber[tablechoice[i]-1] and rwager[i] >= Rminbet:
                    Rplayermoneychanges.append(30 * rwager[i])
                    Rcasinomoneychanges.append(0)
                else:
                    Rplayermoneychanges.append(0)
                    Rcasinomoneychanges.append(rwager[i])
            CasinoRouletteEarn=sum(Rcasinomoneychanges)
            rouletteprofit += CasinoRouletteEarn
            rouletteprofit -= sum(Rplayermoneychanges)
            Ccorrectnumber=[]
            for i in range(0,craps_tables):
                dicerolled=random.randint(1,6)+random.randint(1,6)
                Ccorrectnumber.append(dicerolled)
            Cplayermoneychanges = []
            Ccasinomoneychanges = []
            for i in range(0,len(cguess)):
                if cguess[i] == Ccorrectnumber[tablechoice[i]-1] and cwager[i] >= Cminbet:
                    Cplayermoneychanges.append(craps.payouts(Ccorrectnumber[tablechoice[i]-1])*cwager[i])
                    Ccasinomoneychanges.append(0)
                else:
                    Cplayermoneychanges.append(0)
                    Ccasinomoneychanges.append(cwager[i])
            CasinoCrapsEarn=sum(Ccasinomoneychanges)
            crapsprofit += CasinoCrapsEarn
            crapsprofit -= sum(Cplayermoneychanges)
            TCasinoNightChange = CasinoRouletteEarn+CasinoCrapsEarn
            casinocash += TCasinoNightChange
            for i in range(0,len(plist)):
                PlayerMoney[i] += Rplayermoneychanges[i]
                PlayerMoney[i] += Cplayermoneychanges[i]
        endplayermoney=sum(PlayerMoney)
        playerprofit = endplayermoney-Playerchipsamount
        endlossfromp += playerprofit
        costofbartenders=200* nbartend
        casinocash -= costofbartenders
        casinocashvector.append(casinocash)
    casinocash -=endlossfromp
    casinocashprofit = casinocash-casinoday1cash
    employeeearnings = 0.005*casinocashprofit*nemployees
    casinocashprofit -= employeeearnings
    if returntype=="Graph":
        return(casinocashvector)
    elif returntype=="Tips":
        print("There were "+str(purchaseddrinks)+" drinks purchased.")
        return(totaltips)
    elif returntype=="Game Profit":
        return([crapsprofit,rouletteprofit])
    else:
        return(casinocashprofit)



test1 = CasinoSimulation(Nights,ncust,casinostartcash,barmen,roulette_tables,craps_tables,"Casino")
print(test1)

#test = CasinoSimulation(Nights,ncust,casinostartcash,barmen,roulette_tables,craps_tables,"Graph")
#x_series = [i for i in range(0,Nights)]
#plt.plot(x_series,test)
#plt.show()

rouletteorcraps = CasinoSimulation(Nights,ncust,casinostartcash,barmen,roulette_tables,craps_tables,"Game Profit")
print(rouletteorcraps)


bartips = CasinoSimulation(Nights,ncust,casinostartcash,barmen,roulette_tables,craps_tables,"Tips")
print(bartips)
#print(bartips/Nights)
#print((bartips/Nights)/barmen)




'''
1000 nights profit: $429,068,046.24.

Bonus #1: Should the casino invest more in craps or roulette?

ANSWER: The roulette table profits over 1000 nights is $422,239,497. For craps, it is $96,236,049.28. It's safe to
say that roulette is the better investment at this point.

Bonus #2: How much tips do barmen usually get?

ANSWER: 4 barmen received $1,500,505 in 1000 nights. That is $1,500.51 per night. Which means each bartender
makes about 375.13 in tips each night. The average tip amount was $10.

Bonus #3: How far can they increase or decrease the amount you win on a correct bet in craps and roulette?

ANSWER: For increase, only to the actual odds. For roulette, a payoff of 37 to 1 is when the casino make expected
profit of 0. For craps, it's when the same type but, i.e. for a payout of betting on 2, the payout would be
36 times the wager. With a sim, there's no way to determine when players stop playing based on payoff structure.

Bonus #4: Should there be more bachelors?

Answer: With 10%, the casino profit is $296,931,893.48 and that is with free money of $200. With 20% bachelors
(the new player percentage dropped to 30%), the casino profit is $436,424,716.44. At 30%, the profit is
$1,023,394,530.78. At 40% bachelors, the profit is $277,429,035.96. This would means that the casino
should attract more bachelors, but only until around 30%. If the assumption is that the returning player
percentage stays at 50%, the casino certainly wants more bachelors than regular new players.

Now to changing the free budget. Let's hold the bachelor percentage at 30%. By doing this, we can try
to find the max combination for the casino. Increasing the budget to $300 increases the profit to the casino.
Decreasing the budget to $100 also decreases the profit. Increasing the amount does seem to help certainly.
'''