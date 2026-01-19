# Contagem de numeros pares entre 1 e 50
from os import system

system('cls')
print('{:=^40}'.format(' Contagem de numeros pares entre 1 e 50 '))
for c in range(2, 51, 2): # Contagem de 2 até 50 com passo de 2
    print(c, end=' ') # Imprime os numeros pares

