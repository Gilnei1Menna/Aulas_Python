dados = dict()
list_dados = list()
soma = media = totm = 0
maior_m = list()
while True:
    dados.clear()
    dados['nome'] = str(input('Digite o nome: '))
    while True:
        dados['sexo'] = str(input('Digite o sexo [M/F]: ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('[== ERRO ==]...tente novamente.')
    dados['idade'] = int(input('Digite a idade: '))
    list_dados.append(dados.copy())
    while True:
        pergunta = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if pergunta in 'SN':
            break
        print('[== ERRO ==]...tente novamente.')
    if pergunta == 'N':
        break
    soma += dados['idade']
    media = soma  / len(list_dados)
    if dados['sexo'] == 'F':
        totm += 1
    if dados['idade'] > media:
        maior_m.append(dados.copy())
    if pergunta != 'S':
        print('FIM')
        break
print(list_dados)
print(f'Foram cadastradas {len(list_dados)} pessoas.')
print(f'A média de idade do grupo é de {media:.1f} anos.')
print(f'O total de mulheres é de {totm}: ', end='')
for p in list_dados:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print(f'A lista de pessoas com idade maior que a média é: ', end='')
for p in list_dados:
    if p ['idade'] >= media:
        print(f'{p["nome"]} ', end='')