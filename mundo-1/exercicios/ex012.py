preco_prod = float(input('Informe o valor do produto: R$'))
print(f'Valor do produto sem desconto é: R${preco_prod:.2f}')
desconto_prod = float(input('Informe a porcentagem do desconto:'))
print(f'Foi aplicado um desconto de:{desconto_prod:.2f}%')
valor_desconto = (preco_prod * desconto_prod) / 100
print(f'Você obteve um desconto de: R${valor_desconto:.2f}')
preco_final = preco_prod - valor_desconto
print(f'Total a pagar: R${preco_final:.2f}')
