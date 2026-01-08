vel = float(input('Qual a velocidade atual do carro? '))
if vel > 80:
    print('Atenção! radar de velocidade a frente...')
    print('Voce ultrapassou o limite de  velocidade ')
    multa = (vel - 80) * 7
    print(f'E vai receber uma multa de R${multa:.2f} ')