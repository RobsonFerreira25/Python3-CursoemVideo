reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('As retas formam um triângulo.')
    if reta1 == reta2 ==reta3:
        print('Equilátero')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('As retas nao formam um triangulo')
