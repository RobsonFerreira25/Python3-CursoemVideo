altura = float(input('Informe a altura em metros: '))
largura = float(input('Informe a largura em metros: '))
rendimento_tinta = 2
area = altura * largura
print(f'Sua parede tem {area}m²')
litros_tinta = area / rendimento_tinta
print(f'A quantidade de tinta necessária para pintar {area}m² \nde parede é: {litros_tinta:.2f} litros de tinta')