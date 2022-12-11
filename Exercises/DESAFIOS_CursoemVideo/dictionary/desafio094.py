dados = dict()
list_dados = list()
soma = media = totm = 0
maior_m = list()
while True:
    dados['nome'] = str(input('Digite o nome: '))
    dados['sexo'] = str(input('Digite o sexo [M/F]: ')).upper()[0]
    dados['idade'] = int(input('Digite a idade: '))
    list_dados.append(dados.copy())
    pergunta = str(input('Quer continuar? [S/N]: ')).upper()[0]
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
print(f'O total de mulheres é de {totm}.')
print(f'A lista de pessoas com idade maior que a média é: {maior_m[:]}')