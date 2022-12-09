sal = float(input('Qual o seu salário: R$'))
if sal > 1250:
    print('Com o aumento de 10% o seu salário sera de R${:.2f} '.format((sal * 10 / 100) + sal))
else:
    print('O seu salário com o aumento de 15% é igual a R${:.2f} '.format((sal * 15 / 100) + sal))



