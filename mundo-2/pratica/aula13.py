# Estrutura de repeticao "FOR"
from os import system

system('cls')
# Contagem progressiva
print(f'{' Contagem Progressiva ':=^40}')
for c in range(0, 11):
    print(c)

# Contagem regressiva
print(f'{' Contagem regressiva ':=^40}')
for c in range(10, -1, -1):
    print(c)

# Contagem progressiva com passo de 2
print(f'{" Contagem Progressiva com passo de 2 ":=^40}')
for c in range(0, 11, 2):
    print(c)

# Contagem regressiva com passo de 2
print(f'{" Contagem Regressiva com passo de 2 ":=^40}')
for c in range(10, -1, -2):
    print(c)

# Soma de todos os números
print(f'{" Soma de todos os números ":=^40}')
soma = 0
for c in range(0, 5):
    soma += c
    print(c)
print(f'A soma de todos os numeros é: {soma}')

system('pause')