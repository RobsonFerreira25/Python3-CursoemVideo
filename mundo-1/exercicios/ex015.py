km = float(input('Quantos km você utilizou? '))
dias = int(input('quantos dias você utilizou? '))
total_pagar = (km * 0.15) + (dias * 60)
print(f'O total a ser pago é: {total_pagar:.2f}')
