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
