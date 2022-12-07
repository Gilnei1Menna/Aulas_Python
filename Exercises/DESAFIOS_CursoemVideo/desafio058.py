from random import randint
n1 = int(input('Digite um número: '))
n2 = randint(0, 10)
cont = 0
while n1 != n2:
    n1 = int(input('[ERROU]... Tente novamente: '))
    cont += 1
if n1 == n2:
    print(f'''Você venceu e precisou de apenas {cont + 1} tentativas.
O computador pensou no número {n2}.''')
