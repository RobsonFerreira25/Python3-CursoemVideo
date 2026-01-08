frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece: ', frase.count('A'), 'vezes na frase.')
print('A letra "A" aparece a primeira vez na posição', frase.find('A') + 1)
print('A letra "A" aparece pela ultima vez na posição', frase.rfind('A') + 1)
