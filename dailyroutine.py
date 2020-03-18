import random
from datetime import date

def randomroutine():
    exercises1 = ["100 Flexão de braço", "100 Panturrilha", "400 Polichinelo", "200 Agachamento", "200 Abdominal supra"]
    exercises2 = ["200 Abdominal Infra", "400 Joelho alto", "100 Climber", "200 Passada", "100 Salto"]
    a0 = int(len(exercises1))
    b0 = int(len(exercises2))
    a = exercises1
    b = exercises2
    i = 2
    while len(a) > 2:
        a1 = random.choice(a)
        print(a1)
        a.remove(a1)
    while len(b) > 2:
        b1 = random.choice(b)
        b.remove(b1)
        print(b1)


hoje = date.today()

print("Treino desafio do dia {}".format(hoje.strftime("%d/%b/%Y")))
randomroutine()


