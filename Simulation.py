import Roulette
allbets = [10, 24, 36, 0, 11, 24]
allamounts = [10, 85, 120, 65, 150, 122]
Roulette.SimulateGame(allbets, allamounts)
Roulette.SimulateGame(allbets, allamounts)

import craps
crapguesses = [7,9,2,10,3]
crapbets = [50,70,30,40,50]
craps.RollTheDices(crapguesses,crapbets)
craps.RollTheDices(crapguesses,crapbets)




'''craps.RollTheDices(crapguesses,crapbets)
bongo = 0
bingo = 0
for i in range(1,100):
    this = craps.RollTheDices(crapguesses,crapbets)
    bingo += sum(this[1])
    bongo += this[0]
print(bongo)
print(bingo)
tbets= sum(crapbets)*99
print((bingo-bongo)/tbets)
'''