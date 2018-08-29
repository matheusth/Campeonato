from Campeonato import Campeonato
from Time.Time import Time
champ = Campeonato("NBA", 1990)

champ.addTeams(Time("Teste1", 1991, "Basquete"))
champ.addTeams(Time("Teste2", 1992, "Basquete"))
champ.addTeams(Time("Teste3", 1995, "Basquete"))
champ.addTeams(Time("Teste4", 1998, "Basquete"))
champ.addTeams(Time("Teste5", 1998, "Basquete"))

champ.addTeams(Time("Teste6", 1991, "Basquete"))
champ.addTeams(Time("Teste7", 1992, "Basquete"))
champ.addTeams(Time("Teste8", 1995, "Basquete"))
champ.addTeams(Time("Teste9", 1998, "Basquete"))
champ.addTeams(Time("Teste#", 1998, "Basquete"))
champ.addTeams(Time("Teste*", 1998, "Basquete"))
champ.printMatches()