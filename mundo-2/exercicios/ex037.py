# Tranforme um numero decimal em binario, octal e hexadecimal

numero = int(input('Digite um numero: '))
print('Escolha uma das bases para conversão: ')
opcao = int(input('Digite a opção desejada 1, 2 ou 3: '))
if opcao == 1:
    print(f'O número {numero} será convertido para binario e o resultado é {bin(numero)[2:]}')
elif opcao == 2:
    print(f'O número {numero} será convertido para octal e o resultado é {oct(numero)[2:]}')
elif opcao == 3:
    print(f'O número {numero} será convertido para hexadecimal e o resultado é {hex(numero)[2:]}')
else:
    print('Opção invalida! Tente novamente.')
