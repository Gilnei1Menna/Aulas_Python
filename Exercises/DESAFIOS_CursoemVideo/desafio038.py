n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print('O primeiro valor é \033[1;31m[MAIOR]\033[m')
elif n2 > n1:
    print('O segundo valor é \033[1;31m[MAIOR]\033[m')
else:
    print('\033[4;33mNão existe valor maior, os dois  valores são iguais\033[m')
