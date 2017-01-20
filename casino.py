
import random

roulette_tables=2
craps_tables=2
barmen=1
bartender_wage = 200
casinostartcash=50000
ncust=10
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

    def chips(self):
        self.chips = random.randint(100, 300)
        return (self.chips)

class New(Customer):

    def chips(self):
        self.chips = random.randint(200,300)
        return(self.chips)

class Bachelor(Customer):
    def chips(self):
        self.chips = random.randint(200,500)+freebudget
        return(self.chips)

class Casino(object):
    def __init__(self,id):
        self.id = id
    '''def money(self):
        if day == 1:
            casinomoney=casinostartcash
        else:
            casinomoney += casinowinnings'''

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

playerlist=[]
for i in range(0,10):
    playerlist.append("Player"+str(i+1))

print(playerlist)

for i in range(ncust):
    rando=random.randint(1,10)

    if rando<6:
        playerlist[i]=Returner(str(playerlist[i]))
    elif rando==7:
        playerlist[i] = Bachelor(str(playerlist[i]))
    else:
        playerlist[i] = New(str(playerlist[i]))

print(playerlist[0].chips)