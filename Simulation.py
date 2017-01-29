import Roulette
from collections import Counter
import numpy as np
import random
import craps
import casino
from matplotlib import pyplot as plt

#The guesses
allbets = [10, 24, 36, 0, 11, 24]
#The wagers
allamounts = [10, 85, 120, 65, 150, 122]
#Running the roulette game twice
Roulette.SimulateGame(allbets, allamounts)
Roulette.SimulateGame(allbets, allamounts)



#Craps guesses
crapguesses = [7, 9, 2, 11, 3]
#The wagers for craps
crapbets = [50, 70, 30, 40, 50]
#Simulating a game of craps
craps.SimulateGame(crapguesses, crapbets)
craps.SimulateGame(crapguesses, crapbets)

listofrolls=[]
for i in range(0,1000):
    listofrolls.append(craps.Dices())
labels, values = zip(*Counter(listofrolls).items())
indexes = np.arange(len(labels))
width=1
plt.bar(indexes,values,width)
plt.xticks(indexes+width*0.5,labels)
plt.show()

#Setting the parameters
Nights = 1000
roulette_tables = 10
craps_tables = 10
barmen = 4
bartender_wage = 200
casinostartcash = 50000
ncust = 100
pctreturn = 0.5
pctbach = 0.1
pctnew = 0.4
freebudget = 200
#Simulation of casino based on parameters given
random.seed(3456)
BigSim = casino.CasinoSimulation(Nights, ncust, casinostartcash, barmen, roulette_tables, craps_tables, freebudget, pctreturn, pctbach)
#Graphing the money changes
x_series = [i for i in range(0,Nights)]
plt.plot(x_series, BigSim)
plt.show()
#Which makes a larger profit? Roulette or craps?
random.seed(3456)
Bonus1 = casino.gameprofits(Nights,ncust,casinostartcash,barmen,roulette_tables,craps_tables,freebudget,pctreturn,pctbach)
print(Bonus1)
#The amount of tips a bartender makes
random.seed(3456)
Bonus2 = casino.bartendertips(Nights,ncust,casinostartcash,barmen,roulette_tables,craps_tables,freebudget,pctreturn,pctbach)
print(Bonus2)