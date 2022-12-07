preco = float(input('Digite o preço do produto: '))
des = float(input('Digite o valor do desconto: '))
print('O preço é R$ {:.2f}'.format(preco))
rdes = des * preco / 100
print('\033[mO desconto é de R$ {:.2f}'.format(rdes))
res = preco - rdes
print('E o novo valor fica R$ {:.2f} com o desconto de 5%'.format(res))