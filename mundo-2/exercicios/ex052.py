# Ler um número inteiro e dizer se ele é primo ou não
from os import system
system('cls')
n1 = int(input('Digite um número: '))
for c in range(2, n1):
    if n1 % c == 0:
        print(f'{n1} não é primo')
        break
else:
    print(f'{n1} é primo')
system('pause')