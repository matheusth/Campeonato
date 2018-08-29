from Time.Time import Time
import datetime
import random
class Campeonato:
    def __init__(self,name,year):
        self.name = name
        self.year = year
        self.teams = []

    def addTeams(self,teams):
        self.teams.append(teams)


    #Gera as partidas e retorna um array.
    def genarateMatches(self):
        aux = self.teams.copy()

        rep = len(self.teams)//2
        matches = list(list())
        for i in range(0,rep):
            key = random.randint(0,len(aux)-1)
            a = aux[key]
            aux.pop(key)
            key = random.randint(0, len(aux) - 1)
            b = aux[key]
            aux.pop(key)
            matches.append([a,b])
        if(len(aux) > 0):
            matches.append([aux[0],None])
        return matches

    #chama o metodo genarateMatches() e imprime as partidas.
    def printMatches(self):
        mats = self.genarateMatches();
        for a in mats:
            if(a[1] != None):
                print("%s vs %s"%(a[0],a[1]))
            else:
                print("%s sobrou."%a[0])
