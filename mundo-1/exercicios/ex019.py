from random import choices

alunos  = ['Arthur', 'José', 'Vania', 'Maria', 'Jessica']
nome_sorteado = choices(alunos)
print(f'O aluno sorteado foi {nome_sorteado}')
