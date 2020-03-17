import secrets
import string

print("Vamos criar três senhas aleatórias. Quantos caracteres você quer que elas tenham? (Entre 6 e 20)")
i = int(input())
while i < 6 or i >20:
    print("A senha deve ter entre 6 e 20 caracteres. Quantos caracteres você quer?")
    i = int(input())
else:
    print("Gerando uma senha:")
    print("Primeira senha é: ", secrets.token_urlsafe(i))
    print("Segunda senha é: ", secrets.token_urlsafe(i))
    print("Terceira senha é: ", secrets.token_urlsafe(i))