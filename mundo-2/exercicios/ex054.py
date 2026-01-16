# ler 7 datas de nascimento e mostrar quantas são maiores de idade
from datetime import date
atual = date.today().year
from os import system
system('cls')
maior = 0
menor = 0

for c in range(7):
    data_nascimento = int(input('Digite sua data de nascimento: '))
    idade = atual - data_nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas são maiores de idade e {menor} pessoas são menores de idade')