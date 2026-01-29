# PA com while
from os import system
system('cls')

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro_termo
cont = 1
while cont <= 10:
    print(termo, end=' -> ')
    termo += razao
    cont += 1
print('FIM')
