'''lista = []
pergunta = ''
while True:
    lista.append(int(input('Digite um valor: ')))
    print('Adicionado com sucesso!')
    pergunta = str(input('Quer continuar? [S/N]')).upper()
    if pergunta != 'S':
        lista.sort()
        print(f'Você adicionou os valores: {lista}')
        break'''


'''
lista = []
cont = 0
valor_rep = False
while True:
    valor = int(input('Digite um valor: '))
    if cont == 0:
        lista.append(valor)
        print('Adicionado com sucesso!')
    else:
        for v in lista:
            if v == valor:
                valor_rep = True
        if valor_rep == True:
            print('Esse valor já existe.')
            valor_rep = False
        else:
            valor.append(valor)
            print('Valor adicionado com sucesso!')
    cont += 1
    pergunta = str(input('Quer continuar? [S/N]')).upper()
    if 'N' in pergunta:
        break
lista.sort()
print(f'Você adicionou os valores: {lista}')'''


'''listanum = []
cont = 0
valrep = False
while True:
    num = int(input('Digite um valor: ')) # usuário digita um valor
    if cont == 0:
        listanum.append(num)
        print('Valor adicionado com sucesso!')
    else:
        for valor in listanum: # fazer varredura dentra da lista p/ saber se o num já está lá
            if valor == num:
                valrep = True
        if valrep == True:
            print('Esse valor já foi inserido.')
            valrep = False
        else:
            listanum.append(num)
            print('Valor adicionado com sucesso!')
    cont += 1
    run = str(input('Deseja continuar? [S/N]: ')).upper().split()[0]
    if run != 'S':
        break
listanum.sort()
print(f'Sua lista final, em ordem crescente ficou assim: \n{listanum}.')'''


