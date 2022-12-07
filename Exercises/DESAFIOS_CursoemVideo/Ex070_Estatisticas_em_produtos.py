soma = totmil = menor = cont = 0
barato = ''
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: '))
    cont += 1
    soma += preco

    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    parar = ' '
    while parar not in 'SN':
        parar = str(input('Quer continuar? [S/N]: ')).upper()
    if parar == 'N':
        break
print(f'Total da compra: R${soma:.2f}')
print(f'{totmil} produtos custam mais de R$1000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')


