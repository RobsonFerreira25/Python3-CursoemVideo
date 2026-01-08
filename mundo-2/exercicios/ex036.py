valor_casa = float(input('Digite o valor da casa: '))
valor_salario = float(input('Digite o valor do salário:'))
anos_financiamento = int(input('Digite a quantidade de anos que deseja financiar: '))
numero_parcelas = anos_financiamento * 12
print(f'Em {anos_financiamento} anos você pagará {numero_parcelas} parcelas.')
valor_parcela = valor_casa / numero_parcelas
print(f'O valor da parcela será de R${valor_parcela:.2f}')
if valor_parcela <= 0.3 * valor_salario:
    print(f'Parabéns! Você foi aprovado no financimento da casa.')
else:
    print(f'Infelismente você não foi aprovado no financiamento da casa.')
