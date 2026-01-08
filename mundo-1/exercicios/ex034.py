salario = float(input("Informe seu salário: "))
if salario >= 1250:
    salario = ((salario * 10) / 100) + salario
    print(f'Você vai receber 10% de aumento seu salário atual e:  R${salario:.2f}')
if salario <= 1250:
    salario = ((salario * 15) / 100) + salario
    print(f'Você vai receber 15% de aumento seu salário é:  R${salario:.2f}')