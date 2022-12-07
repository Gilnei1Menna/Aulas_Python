vel = float(input('Velocidade do veiculo: '))
if vel > 80:
    print('[MULTADO]')
    print('---------')
    print('calculando valor da multa: ...')
    print('O valor da sua multa é de: R${:.2f} '.format(vel * 7))
