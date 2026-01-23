from os import system
system('cls')

sexo = str(input('Digite o seu sexo [M/F]: ')).upper()
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, por favor, digite o seu sexo [M/F]: ')).upper()
    if sexo == '':
        sexo = str(input('Dados invalidos, por favor, digite o seu sexo [M/F]: ')).upper()
print(f'sexo {sexo} registrado com sucesso!')
