maior = 0
menor = 0
for c in range(7):
    n = int(input('Digte o ano de nascimento: '))
    if 2022 - n >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas são maiores de idade, e {menor} são menores.')
