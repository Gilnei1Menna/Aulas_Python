tup = tuple(int(input(f'Digite o {c}° valor: ')) for c in range(1, 5))

print(f'Você digitou os valores {tup}')

print(f'O valor 9 aparece {tup.count(9)} vezes')

if 3 in tup:
    print(f'O valor 3 aparece na {tup.index(3)+1}° posição')
else:
    print('Não foi digitado valor 3')

print('Os números pares foram: ', end='')
for n in tup:
    if n % 2 == 0:
        print(f'{n} ', end='')


