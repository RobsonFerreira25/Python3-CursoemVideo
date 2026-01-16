# Ler uma frase e dizer se ela é um palíndromo
from os import system
system('cls')
frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.replace(' ', '')
frase = frase.split()
frase = ''.join(frase)
frase = frase[::-1]
if frase == frase[::-1]:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')
system('pause')