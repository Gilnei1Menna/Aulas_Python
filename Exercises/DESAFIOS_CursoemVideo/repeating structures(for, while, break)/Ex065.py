res = 'S'
cont = 0
soma = 0
media = 0
maior = 0
menor = 0
while res == 'S':
    num = int(input('Digite um valor: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    res = str(input('Quer continuar? [S/N]: ')).upper()
    media = soma / cont
print('A soma entre os {} números é {} e a média é {:.2f}'.format(cont, soma, media))
print('O maior número é {} e o menor é {}'.format(maior, menor))


