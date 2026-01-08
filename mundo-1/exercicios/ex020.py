from random import shuffle
'''
alunos = []

aluno = input('Qual o nome do aluno? ')
alunos.append(aluno)

aluno = input('Qual o nome do aluno? ')
alunos.append(aluno)

aluno = input('Qual o nome do aluno? ')
alunos.append(alunos)

aluno = input('Qual o nome do aluno? ')
alunos.append(aluno)

random.shuffle(alunos)
print(f'Foram adicionados os seguintes alunos: \n{alunos}')

print('=' * 40)
print('Resolução do curso em video.')
'''
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem de apresentação é: ')
print(f'{lista}')
