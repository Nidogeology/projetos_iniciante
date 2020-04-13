raio = float(input('Digite o valor do raio do círculo em centímetros: '))
PI = 3.1415

area = (raio ** 2) * PI
circunferencia = 2 * PI * raio

print(f'O círculo de raio {raio} cm possui área de {area:.2f} cm² \n '
      f'e circunferência de {circunferencia:.2f} cm.')