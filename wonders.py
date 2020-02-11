from random import seed
from random import randint
allWonders = {}
allCivs = {}
allPlayers = []
class players(object):
    def __init__(self, name):
        self.name = name
def promptUser(prompt):
    print(prompt, end = '\n')
    return input("> ")
def getData(filename, dictionary):
    with open(filename, "r") as file:
        for line in file:
            a = line.split("\t")
            dictionary[a[0]] = int(a[1])
def giveRandCiv(player):
    civs = list(allCivs.keys())
    player.civ = civs[randint(0, len(civs) - 1)]
    player.score += (6 - allCivs.pop(player.civ))
def outputList(l):
    for i in l:
        print(i, end = ", ")
seed(promptUser("Input random seed:"))
getData("civ.txt", allCivs)
getData("wonders.txt", allWonders)
for i in range(int(promptUser("Input total players"))):
    allPlayers.append(players(promptUser("Input name of player {}".format(i + 1))))
    allPlayers[i].wonders = []
    allPlayers[i].civ = ''
    allPlayers[i].score = 0
while len(allPlayers) > 0:
    if len(allPlayers) == 1:
        currentPlayer = allPlayers.pop(0)
    else:
        currentPlayer = allPlayers.pop(randint(0, len(allPlayers) - 1))
    giveRandCiv(currentPlayer)
    totalWonders = 0
    wonders = list(allWonders.keys())
    while totalWonders <= 7 or currentPlayer.score < 30:
        if len(wonders) == 1:
            newWonder = wonders.pop(0)
        elif len(wonders) == 0:
            break
        else:
            newWonder = wonders.pop(randint(0, len(wonders) - 1))
        currentPlayer.wonders.append(newWonder)
        if allWonders.get(newWonder, 0):
            currentPlayer.score += (6 - allWonders.pop(newWonder))
        totalWonders += 1
    print("{} is {} and has wonders: ".format(currentPlayer.name, currentPlayer.civ), end = "")
    outputList(currentPlayer.wonders)
    print("\n")
    print("He has a score of {}\n\n".format(currentPlayer.score))
print("Wonders still up for grabs:")
outputList(list(allWonders.keys()))
input("")
