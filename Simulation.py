import Roulette
import craps
import casino
from matplotlib import pyplot as plt

# The guesses
allbets = [10, 24, 36, 0, 11, 24]
# The wagers
allamounts = [10, 85, 120, 65, 150, 122]
# running the roulette game twice
Roulette.SimulateGame(allbets, allamounts)
Roulette.SimulateGame(allbets, allamounts)

# craps guesses
crapguesses = [7, 9, 2, 10, 3]
# the wagers for craps
crapbets = [50, 70, 30, 40, 50]
# simulating a game of craps
craps.SimulateGame(crapguesses, crapbets)


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
#simulation of casino based on parameters given
BigSim=casino.CasinoSimulation(Nights,ncust,casinostartcash,barmen,roulette_tables,craps_tables,freebudget,pctreturn,pctbach)
#graphing the money changes
x_series = [i for i in range(0,Nights)]
plt.plot(x_series,BigSim)
plt.show()
#which makes a larger profit? roulette or craps?
Bonus1=casino.gameprofits(Nights,ncust,casinostartcash,barmen,roulette_tables,craps_tables,freebudget,pctreturn,pctbach)
print(Bonus1)
#the amount of tips a bartender makes
Bonus2=casino.bartendertips(Nights,ncust,casinostartcash,barmen,roulette_tables,craps_tables,freebudget,pctreturn,pctbach)
print(Bonus2)