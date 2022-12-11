lista = dict()
while True:
    lista['nome'] = str(input('Nome: '))
    lista['ano_n'] = int(input('Ano de nascimento: '))
    lista['CTPS'] = int(input('N° CTPS: '))
    idade =  2022 - lista['ano_n']
    lista['idade'] = idade
    if lista['CTPS'] != 0:
        lista['ano_cont'] = int(input('Ano de inicio da CTPS: '))
        lista['salario'] = float(input('Sálario médio do colaborador: '))
        apos = (lista['ano_cont'] + 35) - 1993
        falt = apos - idade
        print(f'O colaborador {lista["nome"]} vai se aposentar com {apos} anos.')
        print(f'Faltam {falt} anos.')
    else:
        print(f'O colaborador {lista["nome"]} não tem uma CTPS cadastrada.')
    pergunta = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if pergunta != 'S':
        print('[CADASTROS FINALIZADOS]')
        break