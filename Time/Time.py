
import datetime


class Time:
    def __init__(self,nome,anoFundado,esporte,atleta = None):
        self.nome = nome
        self.anoFundado = anoFundado
        self.esporte = esporte
        self.quantidadeAtletas = 0
        self.listaAtletas = []
        if (atleta != None):
            self.listaAtletas.append(atleta)
            self.quantidadeAtletas += 1

    def idade(self):
        return datetime.datetime.now().year-self.anoFundado

    def addAtleta(self,atleta):
        self.listaAtletas.append(atleta)
        self.quantidadeAtletas = len(self.listaAtletas)

    def imprimirListaAtletas(self):
        for a in self.listaAtletas:
            print(a)

    def imprimirQuantidadeAtletas(self):
        print("Quantidade de Atletas: %i"%self.quantidadeAtletas)

    def __str__(self):
        return ("%s(%i)"%(self.nome,self.anoFundado))