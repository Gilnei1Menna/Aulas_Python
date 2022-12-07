maior = menor = 0
for c in range(7):
    n = int(input(f'Digte o ano de nascimento da {c+1}° pessoa: '))
    if 2022 - n >= 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas são maiores de idade, e {menor} são menores.')
