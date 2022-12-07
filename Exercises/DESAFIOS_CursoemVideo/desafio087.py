matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma_tc = soma_par = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o [{l}],[{c}] valor: '))

        soma += matriz[l][c]  # Soma todos os valores da matriz

        soma_tc += matriz[l][2]  # Soma os valores da terceira coluna

        if matriz[l][c] % 2 == 0:  # Soma os valores pares
            soma_par += matriz[l][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'A soma de todos os valores digitados é {soma}')
print(f'A soma apenas dos valores pares é {soma_par}')
print(f'A soma da terceira coluna é {soma_tc}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')

