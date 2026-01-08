# Jokenpô
import random
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