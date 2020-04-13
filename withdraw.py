dinheiro = [100, 50, 25, 10, 5, 2, 1, 0.5, 0.25, 0.10, 0.05, 0.01]
newvalue = float(input('Qual valor você deseja sacar em reais? '))
print("Você irá sacar:")
for i in dinheiro:
      x = int(newvalue//i)
      if i > 1 and x != 0:
            print(f'{x} nota(s) de R$ {i:.2f}')
      elif i <= 1 and x != 0:
            print(f'{x} moeda(s) de R$ {i:.2f}')
      newvalue = newvalue % i
