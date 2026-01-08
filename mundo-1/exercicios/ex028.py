from random import randint
from time import sleep

print('Olá, bem vindo ao jogo de adivinhação')
print('Estou pensando em um número, tente adivinhar...')
num = int(randint(1, 5))
resp = int(input('Digite um número de 1 a 5: '))
print('PROCESSANDO...')
sleep(3)
if num == resp:
    print('Parabens você acertou!')
else:
    print(f'Que pena, eu pensei no número {num} e nao no número {resp}.')