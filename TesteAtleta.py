from Time.Atleta import Athlete
from Time.Time import Time

timeA = Time("Time de teste", 1999, "Basquete")
op = 0
while True:
    op = int(input("========================Menu========================\n1-Adicionar Atleta\n2-Ver Idade\n"
                   "3-Quantidade de atletas\n4-Imprimir Atletas\n5-Sair\n"))
    if(op == 5):
        break
    if(op==1):
        timeA.addAtleta(Athlete(input("Digite o nome do atleta: "), int(input("digite a idade: ")), input("Digite o sexo: "),
                                float(input("Digite a altura: ")), float(input("digite o peso: "))))
    elif(op==2):
        print("Idade: %i"%timeA.idade())
    elif(op==3):
        timeA.imprimirQuantidadeAtletas()
    elif (op == 4):
        timeA.imprimirListaAtletas()

