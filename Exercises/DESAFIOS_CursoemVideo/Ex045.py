from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('\033[1;43m[JOKENPÔ]\033[m')
jog = int(input('''Escolha:
\033[1;41m[0]\033[m para pedra \033[1;41m[1]\033[m para papel \033[1;41m[2]\033[m para tesoura
[OPÇÃO] : '''))
print('\033[41mJO\033[m')
sleep(1)
print('\033[41mKEN\033[m')
sleep(1)
print('\033[41mPÔ!!!\033[m')
print('-><-'*12)
if jog == 0 and pc == 0 or jog == 1 and pc == 1 or jog == 2 and pc == 2:
    print('\033[1;42m[EMPATE]\033[m')
    print('Os dois escolheram {}'.format(itens[jog]))
elif jog == 0 and pc == 2 or jog == 1 and pc == 0 or jog == 2 and pc == 1:
    print('\033[1;42m[VITÓRIA]\033[m')
    print('Você jogou \033[1;43m[{}]\033[m vs \033[1;43m[{}]\033[m do computador'.format(itens[jog], itens[pc]))
else:
    print('\033[1;42m[DERROTA]\033[m')
    print('Você jogou \033[1;43m[{}]\033[m vs \033[1;43m[{}]\033[m do computador'.format(itens[jog], itens[pc]))


