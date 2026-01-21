# progressão aritmética
from os import system
system('cls')
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
for c in range(10):
    print(primeiro_termo + c * razao, end=' -> ')
system('pause')
