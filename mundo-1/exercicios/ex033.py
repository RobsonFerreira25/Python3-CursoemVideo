num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))

# Obtendo o número maior
if num1 > num2 and num3:
    numero_maior  = num1
if num2 > num1 and num3:
    numero_maior = num2
if num3 > num1 and num2:
    numero_maior = num3
print(f'O seu número maior é: {numero_maior}')


# Obtendo o número menor
if num1 < num2 and num3:
    numero_menor  = num1
if num2 < num1 and num3:
    numero_menor = num2
if num3 < num1 and num2:
    numero_menor = num3
print(f'O seu número menor é: {numero_menor}')
