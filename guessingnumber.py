import random

numberPC = random.randint(1, 30)
numberUser = int(input("Adivinhe o meu número. Insira um número entre 1 e 30"))
print("Você escolheu o número: {}".format(numberUser))
while numberPC != numberUser:
        if numberUser < numberPC:
            print("Meu número é maior que isso!")
            numberUser = int(input("Tente outro valor:"))
            print("Você escolheu o número: {}".format(numberUser))
        elif numberUser > numberPC:
            print("Meu número é menor que isso!")
            numberUser = int(input("Tente outro valor:"))
            print("Você escolheu o número: {}".format(numberUser))
if numberUser == numberPC:
    print("Você acertou, eu escolhi o número {}".format(numberPC))