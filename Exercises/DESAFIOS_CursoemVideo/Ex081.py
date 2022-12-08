lista = []

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    pergunta = str(input('Quer continuar? ')).upper()[0]

    if pergunta != 'S':
        lista.sort(reverse=True)
        print(f'A lista em ordem decrescente é: {lista}')
        print(f'Foram digitados {len(lista)} números na lista')

        if 5 in lista:
            print('O valor 5 etá na lista', end='')
            print(f'...na posição {lista.index(5)}')
        else:
            print('O valor 5 não foi digitado.')
        break
