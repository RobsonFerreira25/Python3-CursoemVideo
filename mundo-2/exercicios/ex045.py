# Jokenpô
from os import system
from random import randint
'''
print('=-=' * 20)
print('Bem-vindo ao jogo Jokenpô!')
print('=-=' * 20)
print('Escolha sua opção: 1 - Pedra, 2 - Papel, 3 - Tesoura')
escolha_computador = random.randint(1, 3)
escolha_jogador = int(input('Digite sua escolha jogador: '))
if escolha_computador == 1 and escolha_jogador == 2 or escolha_computador == 2 and escolha_jogador == 3 or escolha_computador == 3 and escolha_jogador == 1:
    print('Jogador venceu!')
elif escolha_computador == escolha_jogador:
    print('Empate!')
else:
    print('Computador venceu!')
'''

# Jokenpô 2 resolução do Curso em Video
# Escolha do Computador
system('cls')
print('{:=^40}'.format(' BEM VINDO AO JOGO JOKENPÔ! '))
itens = ('Pedra', 'Papel', 'Tesoura')
print('''
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')

# Escolha do Jogador
jogador = int(input('Digite sua escolha jogador: '))
print(f'Você escolheu {itens[jogador]}')

# Escolha do Computador
computador = randint(0, 2)
print(f'Computador escolheu {itens[computador]}')

# Resultado
if jogador == computador:
    print('Empate!')
elif jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
    print('Jogador venceu!')
else:
    print('Computador venceu!')

system('pause')
