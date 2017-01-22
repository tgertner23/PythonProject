import random
import craps




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

class Casino(object):
    def __init__(self,id):
        self.id = id


class Employee(object):
    def __init__(self,name):
        self.name = name
class Bartender(Employee):

    def fixed_wage(self):
        self.fixed_wage=bartender_wage
        return(bartender_wage)
    #def tips(self):

class Dealer(Employee):

    """def dealerwage(self):
        self.dealerwage"""




'''george = Returner("george")
george.description()
print(george.chips())'''

'''customers=[]
for i in range(0,ncust):
    numero=random.randint(1,10)
    if numero==1:
        customers.append(Bachelor(str(i)))
    elif numero>1 and numero<6:
        customers.append(New(str(i)))
    else:
        customers.append(Returner(str(i)))
'''
def CreatePlayers(nplayers):
    playerlist=[]
    for i in range(0,nplayers):
        playerlist.append("Player"+str(i+1))
    return(playerlist)
def PlayerType(listofplayers):
    ptype = []
    for i in range(0, len(listofplayers)):
        rando=random.randint(1,10)

        if rando<6:
            listofplayers[i]=Returner(str(listofplayers[i]))
            ptype.append("R")
        elif rando==7:
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

simulations = 5
RMinchoices=[50,100,200]
CMinchoices=[0,25,50]



def CasinoSimulation(nights, pnumber,casinoday1cash,nbartend,nroulette,ncraps):
    nemployees=nroulette+ncraps
    endlossfromp=0
    casinocash=casinoday1cash
    for i in range(0,nights):
        plist=CreatePlayers(pnumber)
        playertypes=PlayerType(plist)
        numbachelors=playertypes.count("B")
        casinocash -= (freebudget*numbachelors)
        PlayerMoney = PlayerChips(plist)
        Playerchipsamount=sum(PlayerMoney)
        actionspernight = 12
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
                    drinkcost = tip+20
                    PlayerMoney[i] -= drinkcost
                    drinksorders[i] += 1
                elif drinksorders[i]==1 and drinknumbers[i]==2 and PlayerMoney[i]>60:
                    tip = random.randint(0, 20)
                    drinkcost = tip + 20
                    PlayerMoney[i] -= drinkcost
                    drinksorders[i] += 1
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
            Ccorrectnumber=[]
            for i in range(0,craps_tables):
                dicerolled=random.randint(1,6)+random.randint(1,6)
                Ccorrectnumber.append(dicerolled)
            Cplayermoneychanges = []
            Ccasinomoneychanges = []
            for i in range(0,len(cguess)):
                if cguess[i]== Ccorrectnumber[tablechoice[i]-1] and cwager[i] >= Cminbet:
                    Cplayermoneychanges.append(craps.payouts(Ccorrectnumber)*cwager[i])
                    Ccasinomoneychanges.append(0)
                else:
                    Cplayermoneychanges.append(0)
                    Ccasinomoneychanges.append(cwager[i])
            CasinoCrapsEarn=sum(Ccasinomoneychanges)
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
    casinocash -=endlossfromp
    casinocashprofit = casinocash-casinoday1cash
    employeeearnings = 0.005*casinocashprofit*nemployees
    casinocashprofit -= employeeearnings
    return(casinocashprofit)



test = CasinoSimulation(1000,ncust,casinostartcash,barmen,roulette_tables,craps_tables)
print(test)
