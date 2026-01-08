from math import radians, cos, sin, tan
grau = float(input('Digite o Grau do seu Triângulo retângulo: '))
seno = sin(radians(grau))
cosseno = cos(radians(grau))
tangente = tan(radians(grau))
print(f'Um triângulo retângulo com {grau} graus tem seus valores de: \nSeno: {seno:.2f} \nCosseno: {cosseno:.2f} \nTangente: {tangente:.2f}')

