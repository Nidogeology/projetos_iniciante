cpf = input("Entre com o seu CPF ")
cpflist = []
cpflist = list(cpf)
for digito in cpflist:
    if not digito.isnumeric():
        cpflist.remove(digito)
digito1 = []
for i in range(10, 1, -1):
    digito1 += [i]
digito2 = []
for i in range(11, 1, -1):
    digito2 += [i]
var = 0
for i in range(9):
    var += int(digito1[i] * int(cpflist[i]))
digitof1 = int(11 - (var % 11))
if digitof1 > 9:
    digitof1 = 0
var = 0
for i in range(10):
    var += int(digito2[i]) * int(cpflist[i])
digitof2 = int(11 - (var % 11))
if digitof2 > 9:
    digitof2 = 0
if digitof1 == int(cpflist[-2]) and digitof2 == int(cpflist[-1]):
    print("CPF válido")
else:
    print("CPF inválido")
