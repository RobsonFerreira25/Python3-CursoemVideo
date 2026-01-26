# Jogo de adivinhação v2.0
from os import system
from random import randint
system('cls')

num_pc = randint(0, 10)
escolha_jogador = -1
num_tentativas = 0

print('{:=^50}'.format(' Bem vindo ao jogo de adivinhação! '))
print('Pensei em um número entre 0 e 10. Tente adivinhar!')

while not escolha_jogador == num_pc:
    escolha_jogador = int(input('Digite sua escolha jogador: '))
    num_tentativas += 1
    
    if escolha_jogador == num_pc:
        print(f'Parabens! Voce acertou com {num_tentativas} tentativas!')
    else:
        if escolha_jogador < num_pc:
            print('O numero é maior. Tente mais uma vez.')
        elif escolha_jogador > num_pc:
            print('O numero é menor. Tente mais uma vez.')
