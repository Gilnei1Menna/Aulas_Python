valor = float(input('Digite o valor do produto: '))
pag = int(input('''formas de pagamento:
[1] À vista (dinheiro/cheque: 10% de desconto)
[2] À vista (cartão: 5% de desconto)
[3] Em 2x no cartão (sem juros)
[4] Em 3x ou mais (cartão: 20% de juros)
[[DIGITE UMA OPÇÃO]] : '''))
if pag == 1:
    print('O valor a ser pago é de: {:.2f}'.format(valor - valor * 10 / 100))
elif pag == 2:
    print('O valor a ser pago é de: {:.2f}'.format(valor - valor * 5 / 100))
elif pag == 3:
    print('O valor a ser pago é de: {:.2f} em 2x de {:.2f}'.format(valor, valor / 2))
elif pag == 4:
    vezes = int(input('Em quantas vezes? '))
    print('O valor a ser pago é de: {:.2f} em {}x de {:.2f} '.format(valor + valor * 20 / 100, vezes, (valor + valor * 20 / 100) / vezes))
else:
    print('OPÇÃO INVÁLIDA')