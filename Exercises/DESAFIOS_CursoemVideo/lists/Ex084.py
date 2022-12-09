lista = list()
dado = list()
mai = men = cont = 0

while True:

    dado.append(str(input('Digite o nome: ')))
    dado.append(float(input('Digite o peso [Kg]: ')))

    if len(lista) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]

    lista.append(dado[:])
    dado.clear()
    cont += 1
    print('Cadastro realizado!')
    pergunta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if pergunta in 'Nn':
        break

print('-' * 30)
print(f'Os dados são {lista}')
print(f'Foram cadastradas {cont} pessoas.')  # Eu usei um contador(cont),

print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in lista:
    if p[1] == mai:
        print(f'[ {p[0]} ]')

print('\n')

print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in lista:
    if p[1] == men:
        print(f'[ {p[0]} ]')

