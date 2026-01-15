# Soma dos números impares divisiveis por 3 entre 1 e 500
from os import system
system('cls')
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0: # Verifica se o número é divisível por 3
        soma += c # Soma os números divisiveis por 3
        print(c)
print(f'A soma de todos os números divisiveis por 3 entre 1 e 500 é: {soma}')
system('pause')
