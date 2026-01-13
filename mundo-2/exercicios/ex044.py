'''
# Sistema de pagamento.
# Coleta de dados.
preco_normal_produto = float(input('Digite o preço normal do produto: '))
condicao_pagamento = int(input('Digite a condição de pagamento: '))

# Condições de pagamento.
if condicao_pagamento == 1:
    preco_normal_produto = preco_normal_produto * 0.9
    print(f'Forma de pagamento: dinheiro, valor final: R${preco_normal_produto:.2f}')
elif condicao_pagamento == 2:
    preco_normal_produto = preco_normal_produto * 0.95
    print(f'Forma de pagamento: cartão a vista, valor final: R${preco_normal_produto:.2f}')
elif condicao_pagamento == 3:
    preco_normal_produto = preco_normal_produto
    print(f'Forma de pagamento: cartão parcelado em ate 2x, valor final do produto: R${preco_normal_produto:.2f}')
elif condicao_pagamento == 4:
    preco_normal_produto = preco_normal_produto * 1.2
    print(f'Forma de pagamento: cartão parcelado em 3x ou mais, valor final do produto: R${preco_normal_produto:.2f}')
else:
    print('Opção invalida')
'''

# Forma aprimorada, Curso em Video
print('{:=^40}'.format(' LOJAS KN '))
compras = float(input('Digite o valor das compras: R$'))
print('''
FORMAS DE PAGAMENTO:
[1] À vista dinheiro
[2] À vista cartão 5% de desconto
[3] 2x no cartão sem juros
[4] 3x ou mais no cartão 20% de juros
''')
opcao = int(input('Digite a opção de pagamento: '))
if opcao == 1:
    compras = compras - (compras * 0.1)
    print(f'Pagamento em dinheiro com 10% de desconto, valor final: R${compras:.2f}')
elif opcao == 2:
    compras = compras - (compras * 0.05)
    print(f'Pagamento em cartão a vista com 5% de desconto, valor final: R${compras:.2f}')
elif opcao == 3:
    vparcelas = compras / 2
    print(f'Pagamento em cartão parcelado em 2x SEM JUROS, valor final: R${compras:.2f}')
    print(f'Você pagará R${compras:.2f} em 2 parcelas de R${vparcelas:.2f}')
elif opcao == 4:
    print(f'Pagamento em cartão parcelado em 3x ou mais COM JUROS de 20%')
    nparcelas = int(input('Digite o número de parcelas: '))
    valor_final = compras + (compras * 0.2)
    vparcelas = valor_final / nparcelas
    print(f'Pagamento em cartão parcelado em {nparcelas}x COM JUROS de 20%, valor final: R${valor_final:.2f}')
    print(f'Você pagará R${valor_final:.2f} em {nparcelas}x de R${vparcelas:.2f}')
else:
    print('Opção de pagamento invalida! Tente novamente.')
    