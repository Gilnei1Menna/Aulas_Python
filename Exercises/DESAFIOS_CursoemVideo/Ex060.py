# USANDO O MODO ( WHILE )
num = int(input('Digite um número: '))
cont = num
fat = 1
while cont > 0:
    print(cont, 'x ' if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1
print(f'{fat}')

# USANDO O MODO ( FOR )
num = int(input('Digite um número: '))
fat = 1
for c in range(num, 0, -1):
    print(c, 'x ' if c > 1 else ' = ', end='')
    fat *= c
print(f'{fat}')
