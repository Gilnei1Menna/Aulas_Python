sal = float(input('Qual o seu salário? '))
pau = float(input('Porcentagem do aumento: '))
raum = sal * pau / 100
print('O aumento é de {:.2f} R$'.format(raum))
aum = raum + sal
print('O seu novo sálario oferecido pela empresa é de, {:.2f} R$'.format(aum))
