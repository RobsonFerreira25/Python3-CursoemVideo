'''
km = float(input('Qual a distância em KM da sua viagem? '))
if km <=200:
    print(f'Para uma viagem de {km}KM')
    km = km * 0.50
    print(f'Você pagará R${km:.2f}')
if km > 200:
    print(f'Para uma viagem de {km}KM')
    km = km * 0.45
    print(f'Você pagará R${km:.2f}')
'''

km = float(input('Qual é a distância em KM da sua viagem? '))
print(f'voce está prestes a começar uma viagem de {km}KM.')
if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45
print(f'O preço da sua passagem sera de R${preco:.2f}')
