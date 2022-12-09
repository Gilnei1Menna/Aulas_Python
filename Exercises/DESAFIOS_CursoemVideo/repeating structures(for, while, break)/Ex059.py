from time import sleep
menu = 0
while menu <= 4:
    print('-'*18)
    v1 = float(input('Primeiro valor: '))
    v2 = float(input('Segundo valor: '))

    menu = int(input('''----------------------------------------
        [1] soma
        [2] multiplicação
        [3] maior
        [4] novos valores
        [5] sair
       ESCOLHA UMA OPÇÃO: '''))
    print('-'*40)

    if menu == 1:  # SOMA #
        print('A soma entre {} e {} é igual a {}'.format(v1, v2, v1+v2))
    elif menu == 2:  # MULTIPLICAÇÃO #
        print('A multiplicação de {} e {} é igual a {}'.format(v1, v2, v1*v2))
    elif menu == 3:  # MAIOR #
        if v1 > v2:
            print('O primeiro valor ´maior')
        else:
            print('O segundo valor é maior')
    elif menu == 5:  # SAIR #
        print('[FIM]')
    elif menu > 5:
        print('OPÇÃO INVÁLIDA')
        novo = str(input('Quer digitar novos números? [S/N]: ')).upper()
        if novo in 'S':
            menu = 4
        else:
            print('FIM DO PROGRAMA')
    sleep(2)
