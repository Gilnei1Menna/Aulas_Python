num = int(input('\033[4;30;43mDigite um número inteiro\033[m: '))
print('''\033[1m\033[4mEscolha uma das bases para conversão\033[m:
\033[31m[1]\033[m BINÁRIO
\033[31m[2]\033[m OCTAL
\033[31m[3]\033[m HEXADECIMAL\033[m''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('\033[1;41m[OPÇÃO INVÁLIDA]...tente novamente.\033[m')
