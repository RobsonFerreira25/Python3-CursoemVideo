import datetime
ano_nascimento  = int(input('Digite o ano de nascimento: '))
idade = datetime.datetime.now().year - ano_nascimento
if idade == 18:
    print('Você tem que se alistar imendiatamente.')
elif idade > 18:
    print(f'Você tem {idade} anos e ja passou {idade - 18} do prazo de alistamento.')
elif idade < 18:
    print(f'Você tem {idade} anos e ainda faltam {18 - idade} anos para o alistamento.')
else:
    print('Opção invalida! Tente novamente.')
    
