dias = int(input('Informe  a quantidade de dias do aluguel: '))
km = float(input('Informe quantos Km foram percorridos: '))
res = (km * 0.15) + (dias * 60)
print('O total a pagar pelo aluguel é o valor de R${:.2f}'.format(res))
