num = 1
soma = 0
cont = 0
while num != 999:
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
if num == 999:
    soma -= 999
    cont -= 1
    print('Foram utilizados {} números e a soma entre eles é de {}'.format(cont, soma))
