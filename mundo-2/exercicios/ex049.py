# Tabuada
from os import system
system('cls')
"""
n1 = int(input('Digite um numero: '))
for i in range(11):
    r = n1 * i
    print(f'{n1} X {i} = {r}')
print(f'Essa é a tabuada de {n1}')
"""

# Resolução curso em video
num = int(input('Digite um numero: '))
for c in range (1, 11):
    print(f'{num} X {c:2} = {num * c}')
system('pause')
