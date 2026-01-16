# Ler 6 números inteiros e mostrar a soma apenas dos que forem pares
soma = 0
for c in range(6):
    n1 = int(input('Digite um número: '))
    if n1 % 2 == 0:
        soma += n1
print(f'A soma dos número pares é: {soma}')
