# Ler um número inteiro e dizer se ele é primo ou não
from os import system
system('cls')
"""
n1 = int(input('Digite um número: '))
for c in range(2, n1):
    if n1 % c == 0:
        print(f'{n1} não é primo')
        break
else:
    print(f'{n1} é primo')
"""

num = int(input('Digite um numero: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[33m{c}\033[m', end=' ')
        total += 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')
if total == 2:
    print(f'{num} é primo')
else:
    print(f'{num} não é primo')
system('pause')