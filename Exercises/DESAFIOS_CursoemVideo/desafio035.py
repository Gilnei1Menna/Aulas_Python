print('\033[1;31m-=\033[m'*20)
print('\033[33m[Analizador de triângulos]\033[m')
print('\033[1;31m-=\033[m'*20)
r1 = float(input('\033[1;33mDigite o primeiro seguimento: '))
r2 = float(input('Digite o segundo seguimento: '))
r3 = float(input('Digite o terceiro seguimento:\033[m '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1;31m-<>-\033[m'*10)
    print('\033[1;33;40m[PODEM FORMAR UM TRIÂNGULO]\033[m')
else:
    print('\033[1;31m-<>-\033[m' * 10)
    print('\033[1;31;40m[NÃO PODE FORMAR UM TRIÂNGULO]\033[m')
