saldo_real = float(input('Informe seu saldo em Reais R$: '))
cotacao_dolar = float(input('Informe a cotação atual do Dolar $: '))
saldo_real = saldo_real / cotacao_dolar
print(f'Seu saldo atual em dolar é: ${saldo_real:.2f}')
