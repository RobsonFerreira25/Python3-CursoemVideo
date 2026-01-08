import datetime

ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = datetime.datetime.now().year - ano_nascimento

if idade <= 9:
    print(f'Você tem {idade} de idade e se enquadra na categoria MIRIM.')
elif idade <= 14:
    print(f'Você tem {idade} de idade e se enquadra na categoria INFANTIL.')
elif idade <= 19:
    print(f'Você tem {idade} de idade e se enquadra na categoria JUNIOR.')
elif idade <= 20:
    print(f'Você tem {idade} de idade e se enquadra na categoria SÊNIOR.')
else:
    print(f'Você tem {idade} de idade e se enquadra na categoria MASTER.')