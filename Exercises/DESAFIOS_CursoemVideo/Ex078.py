'''valores = []
for v in range(0, 5):
    valores.append(int(input(f'Digite o {v + 1}° valor: ')))
print(f'Você digitou os valores{valores}')

print(f'O menor valor digitado foi: {min(valores)}', end='')
for pos, val in enumerate(valores):
    if val == min(valores):
        print(f' na posição {pos}')

print(f'O maior valor digitado foi: {max(valores)}', end='')
for pos, val in enumerate(valores):
    if val == max(valores):
        print(f' na posição {pos}')'''

valores = []
mai = men = 0
for v in range(0, 5):
    valores.append(int(input(f'Digite o {v+1}° valor: ')))
    if v == 0:
        mai = men = valores[v]
    else:
        if valores[v] > mai:
            mai = valores[v]
        if valores[v] < men:
            men = valores[v]
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado é {mai} nas posições ', end='')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}...', end='')
print('\n')
print(f'O menor valor digitado é {men} nas posições ', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}...', end='')