cnpj = input("Entre com o seu CNPJ ")

# aqui eu uso o isnumeric() pra remoção de caracteres não numéricos
clist = [i for i in list(cnpj) if i.isnumeric()]

# essa parte para conferir se não é sequencia. nessa parte eu achei
# bem confusa, mas quis fazer com menos linhas possíveis

seq = list(int(i*len(clist)) for i in (str([i for i in range(10)])) if i.isnumeric())
j = ''
for k in clist:
    j += k

# aqui pra gerar os multiplicadores, o código ficaria menor se eu os escrevesse direto
# mas serviu pra praticar, vai que são multiplicadores maiores
d1 = ([i for i in range(5, 1, -1)] + [i for i in range(9, 1, -1)])
d2 = ([i for i in range(6, 1, -1)] + [i for i in range(9, 1, -1)])

# var1 e var2 para calcular o penultimo e ultimo digitos
var1 = sum(int(d1[i]) * int(clist[i]) for i in range(12))
d1 = int(11 - (var1 % 11))
d1 = 0 if d1 > 9 else d1

var2 = sum(int(d2[i]) * int(clist[i]) for i in range(13))
d2 = int(11 - (var2 % 11))
d2 = 0 if d2 > 9 else d2

# e aqui eu checo a validade comparando digitos e se não é sequencia
validade = f'{cnpj} é válido.' if d1 == int(clist[-2]) and d2 == int(clist[-1]) \
                                  and int(j) not in seq else f'{cnpj} é inválido.'

print(validade)