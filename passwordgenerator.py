import random
import string

def generator(i):
    characteres = string.ascii_letters + string.digits
    return ''.join(random.choice(characteres) for i in range(i))

print("Vamos criar três senhas aleatórias. Quantos caracteres você quer que elas tenham? (Entre 6 e 20)")
i = int(input())
while i < 6 or i >20:
    print("A senha deve ser entre 6 e 20 caracteres. Quantos caracteres você quer?")
    i = int(input())
else:
     print("Gerando uma senha:")
     print("Primeira senha é: ", generator(i))
     print("Segunda senha é: ", generator(i))
     print("Terceira senha é: ", generator(i))


