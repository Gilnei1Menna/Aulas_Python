print('Gerador de PA')
print('-='*10)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('[{}]-'.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('[FIM]...progressão finalizada com {} termos'.format(total))

