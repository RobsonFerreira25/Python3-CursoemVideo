# Contagem de numeros pares entre 1 e 50
from os import system

system('cls')
print('{:=^40}'.format(' Contagem de numeros pares entre 1 e 50 '))
for c in range(0, 51, 2): # Contagem de 0 até 50 com passo de 2
    print(c) # Imprime os numeros pares

system('pause')
