lista = ('Arroz', 3.75, 'Feijão', 5.70, 'Café', 13.99, 'Azeite', 8.00, 'Açucar', 2.99)

print('-=' *20)
print(f'{"LISTA DE COMPRAS":^40}')
print('-' *40)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$ {lista[pos]:.2f}')
print('-=' * 20)
