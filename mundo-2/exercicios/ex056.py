from os import system
system('cls')

# Variaveis
idade_homem = 0
idade_mulher = 0
homem_velho = 0
mulher_velha = 0

# laço de repetição para coletar dados de 4 pessoas
for c in range(4):
    
    # coleta de dados
    print(f'----- {c+1}ª PESSOA -----')
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper()
    media_idade = (idade_homem + idade_mulher) / 4
    
    # verificação de homem velho
    if sexo == 'M':
        nome_homem = nome
        idade_homem = idade
        if idade > homem_velho:
            homem_velho = idade
            nome_homem = nome
    
    # verificação de mulher velha
    if sexo == 'F':
        nome_mulher = nome
        idade_mulher = idade
        if idade > mulher_velha:
            mulher_velha = idade
            nome_mulher = nome

print(f'Media de idade: {media_idade}, homem mais velho: {nome_homem}, mulher mais velha: {nome_mulher}')