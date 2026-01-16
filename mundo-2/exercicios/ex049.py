# Tabuada
from os import system
system('cls')
n1 = int(input('Digite um numero: '))
for i in range(11):
    r = n1 * i
    print(f'{n1} X {i} = {r}')
print(f'Essa é a tabuada de {n1}')
system('pause')
