salario_ant = float(input('Informe seu salário atual: R$'))
print(f'O seu salário atual e de: R${salario_ant:.2f} ')
aumento = float(input('Informe a porcentagem de aumento: '))
print(f'Voce recebeu um aumento de: {aumento}%')
cal_salario = (salario_ant * aumento) /100
salario_atual = salario_ant + cal_salario
print(f'Seu salário atual e de: R${salario_atual:.2f}')