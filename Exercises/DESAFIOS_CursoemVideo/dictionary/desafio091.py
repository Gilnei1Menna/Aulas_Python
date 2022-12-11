from random import randint
from time import sleep
from operator import itemgetter
jogo = dict()
ranking = list()
jogo = {'jogador_1': randint(1, 6),
        'jogador_2': randint(1, 6),
        'jogador_3': randint(1, 6),
        'jogador_4': randint(1, 6)}
print(f'{"Valores sorteados:":^27}')
print('-' * 27)
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-' * 27)
print('RANKING:')
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)
print('-' * 42)