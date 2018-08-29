class Athlete:
    def __init__(self,nome,idade,sexo,altura,peso):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura
        self.peso = peso

    def imc(self):
        return self.peso / (self.altura ** 2)

    def __str__(self):
        return ("Nome: %s\nIdade: %i\nSexo: %s\nAltura: %s\nPeso: %s\nIMC: %s"%(self.nome,self.idade,self.sexo,self.altura,self.peso,self.imc()))