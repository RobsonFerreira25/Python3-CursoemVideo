# estrutura condicional aninhada
nome = str(input('Digite um nome: ')).upper()
if nome == 'ROBSON':
    print('Que nome bonito!')
elif nome == 'MARIA' or nome == 'JOAO' or nome == 'JOSE':
    print('Seu nome é bem popular no Brasil')
elif nome in 'ANA MONICA DAVYNA BEATRIZ LAIZ':
    print('Esse nome é lindo')
else:
    print('Seu nome é normal')
print(f'Tenha um bom dia {nome.capitalize()}')
