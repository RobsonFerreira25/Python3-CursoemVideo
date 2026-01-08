# Minha resposta
n1 = int(input('Digite um número: '))
r = 0
for t in range(11):
    r = t * n1
    print(n1, 'X', t, '=' , r)
print('Essa e a tabuada de {}'.format(n1))

'''
# Essa é a forma mais Correta1
n1 = int(input('Digite um numero: '))
for i in range(11):
    r = n1 * i
    print(f'{n1} X {i} = {r}')
print(f'Essa é a tabuada de {n1}')
'''