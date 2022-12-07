r1 = float(input('\033[1;33mDigite o primeiro seguimento: '))
r2 = float(input('Digite o segundo seguimento: '))
r3 = float(input('Digite o terceiro seguimento:\033[m '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1;33;40m[PODEM FORMAR UM TRIÂNGULO]\033[m')
    if r1 == r2 and r2 == r3:
        print('\033[31m[EQUILÁTERO]\033[m') # TODOS OS LADOS IGUAIS
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('\033[31m[ESCALENO]\033[m') # TODOS OS LADOS DIFERENTES
    else:
        print('\033[31m[ISÓSCELES]\033[m') # DOIS LADOS IGUAIS
else:
    print('\033[1;31;40m[NÃO PODE FORMAR UM TRIÂNGULO]\033[m')
