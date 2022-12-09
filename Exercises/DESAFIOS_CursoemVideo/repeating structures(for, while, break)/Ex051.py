print('\033[1m=' * 29)
print('     10 TERMOS DE UMA PA')
print('=' * 29)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = termo + (10 - 1) * razão
for c in range(termo, décimo + razão, razão):
    print(c, end=' → ')
print('ACABOU')


