termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
cont = 1
while cont <= 10:
    print(f'{termo}', end='-> ' if cont < 10 else '...FIM DA PA')
    termo += razão
    cont += 1

