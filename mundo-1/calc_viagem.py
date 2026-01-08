distancia_km = float(input('Digite a distância em KM: '))
velocidade_media_kmh = float(input('Qual a velocidade media no momento? '))
valor_base_reais = float(0.30)

tempo  = (distancia_km / velocidade_media_kmh) * 60
if tempo >= 60:
    print(f'Esse destino vai levar {tempo} minutos.')
else:
    print(f'esse destino vai levar {tempo} minutos.')

valor_tempo  = tempo * valor_base_reais
print(f'Você vai receber R${valor_tempo:.2f}')

valor_minuto = valor_tempo / tempo
print(f'Essa viagem esta pagando R${valor_minuto:.2f}')