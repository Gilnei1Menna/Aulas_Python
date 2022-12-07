valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o saLário do comprador: '))
par = int(input('Digite quantas parcelas a ser pagas: '))
val = valor - valor * 7 / 100
if val / par < salario * 30 / 100:
    print('[APROVADO]')
    print('As parcelas iram ser pagas em {} vezes de R${:.2f} sem juros. '.format(par, val / par))
else:
    print('[REPROVADO]')
    print('As parcelas seriam pagas em {} vezes de R${:.2f} sem juros. '.format(par, val / par))
