# LEIA O PESO DE CINCO PESSOAS, NO FINAL MOSTRE QUAL FOI O MAIOR EO MENOR PESO LIDOS.
maior = menor = cont = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {}° pessoa: '.format(p)))
    cont += 1
    if cont == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {} e o menor peso foi {}'.format(maior, menor))
