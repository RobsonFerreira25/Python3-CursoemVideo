import math
'''
cat_oposto = float(input('Digite o valor do cateto oposto: '))
cat_adjacente = float(input('Digite o valor de cateto adjacente:'))
calc_cat = (cat_oposto**2 + cat_adjacente**2)
print(f'O calculo dos catetos e: {calc_cat}')
hipotenusa = math.sqrt(calc_cat)
print(f'O valor da hipotenusa e: {hipotenusa:.2f}')

print('='*40)
print('Resolução do curso em video sem importação!')

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = (co **2 + ca**2) ** (1/2)
print(f'O valor da hipotenusa é: {hi:.2f}')
'''

print('='*40)
print('Resolução do curso em video com importação!')

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = math.hypot(co, ca)
print(f'O valor da hipotenusa é: {hi:.2f}')
