# while com menus
from os import system

system('cls')

escolha = 0

while escolha != 5:
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))

    print('Escolha uma opção no menu')
    print('[1] Somar, \n[2] Multiplicar, \n[3] Maoir, \n[4] Novos Números, \n[5] Sair do Programa')
    escolha = int(input('Digite sua opção de 1 a 5: '))

    if escolha == 1:
        operacao = valor1 + valor2
        print(f'A opção escolhida: Soma, {valor1} + {valor2} é igual: {operacao}')
    
    elif escolha == 2:
        operacao = valor1 * valor2
        print(f'Operação escolhida: Multiplicação, {valor1} * {valor2} é igual: {operacao}')
    
    elif escolha == 3:
        if valor1 > valor2:
            print(f'O {valor1} é maior que o {valor2}')
        else:
            print(f'O {valor2} é maior que o {valor1}')
    
    elif escolha == 4:
        print('Escolha os numeros novamente!')
        system('cls')
        continue

    elif escolha == 5:
        print('Fim do Programa!')
        break
