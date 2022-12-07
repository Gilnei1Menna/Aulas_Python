dis = float(input('Digite a distãncia da viajem: '))
if dis <= 200:
    print('O valor a ser cobrado é: {}'.format(dis * 0.5))
else:
    print('o Valor a ser cobrado é {}'.format(dis * 0.45))
