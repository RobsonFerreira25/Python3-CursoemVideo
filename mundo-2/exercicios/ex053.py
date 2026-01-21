# Ler uma frase e dizer se ela é um palíndromo
from os import system
system('cls')
"""
frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.replace(' ', '')
frase = frase.split()
frase = ''.join(frase)
frase = frase[::-1]
if frase == frase[::-1]:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')
"""
frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.replace(' ', '')
frase = frase.split()
frase = ''.join(frase)
for c in range(len(frase)):
    if frase[c] != frase[-c - 1]:
        print('Não é um palíndromo!')
        break
else:
    print('É um palíndromo!')
system('pause')