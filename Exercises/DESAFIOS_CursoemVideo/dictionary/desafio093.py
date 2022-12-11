dados = dict()
gol_p = list()
totgol = cont = 0
dados['nome'] = str(input('Nome do jogador: '))
dados['quant_p'] = int(input(f'Quantidade de partidas do {dados["nome"]}: '))
for g in range(dados['quant_p']):
    dados['quant_g'] = int(input(f'Quantos gols o {dados["nome"]} fez na {g+1}° partida? '))
    gol_p.append(dados['quant_g'])
    dados['golp'] = gol_p
    totgol += dados['quant_g']
    dados['quant_g'] = totgol
print('-' *30)

for p in gol_p:
    cont += 1
    print(f'Na partida {cont}, fez {p} gols.')
print('-' * 30)
print(f'O jogador {dados["nome"]} fez um total de {totgol} gols em {dados["quant_p"]} partidas no campeonato.')
print('-' *30)
print(dados)
    

# ['nome'], nome do jogador
# ['quant_p], quantidade de partidas
# ['quant_g], quantidade de gols
# ['golp'], gols por partida 