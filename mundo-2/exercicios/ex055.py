# ler o peso de 5 pessoas e mostrar o maior e o menor peso
from os import system
system('cls')
peso_maior = 0
peso_menor = 0

for c in range(5):
    peso = float(input('Digite o seu peso: '))
    if c == 1:
        peso_maior = peso
        peso_menor = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < peso_menor:
            peso_menor = peso
print(f'O maior peso é {peso_maior} e o menor peso é {peso_menor}')
