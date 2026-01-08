n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
print(f'Sua media é: {m:.1f}')
if m >= 6.0:
    print('Parabens você foi aprovado!')
else:
    print('Que pena estude mais um pouco!')