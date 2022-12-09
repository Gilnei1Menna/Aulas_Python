tabela = 'Palmeiras', 'Inter', 'Fluminense', 'Corinthians', 'Flamengo', 'Athetico Paranaense', 'Atletico Mineiro', \
         'Fortaleza', 'São Paulo', 'América Mineiro', 'Botafogo', 'Santos', 'Goias', 'Bragantino', 'Coritiba',\
         'Cuiabá', 'Ceará', 'Atlético Goianiense', 'Avaí', 'Juventude'

print('{:-^60}'.format(' VAGA DIRETA PRA LIBERTADORES '))
print(f'Os times que garantiram vaga direta para a Libertadores foram {tabela[:6]}')
print('{:-^60}'.format(' REBAIXAMENTO '))
print(f'Os quatro rebaixados foram {tabela[-4:]}')
print('{:*^60}'.format(' ORDEM ALFABÉTICA '))
print('Os times em ordem alfabética são:', sorted(tabela))
print('-=' *30)
time = str(input('Digite um time para saber a posição: '))
print(f'O {time} terminou o campeonato na {tabela.index(time)+1}ª posição')

