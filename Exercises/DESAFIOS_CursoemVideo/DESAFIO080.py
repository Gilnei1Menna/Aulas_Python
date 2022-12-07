# Crie um programa onde o usuário possa digitar cinco VALORES NUMÉRICOS e cadastre-os
# em uma LISTA, JÁ NA POSIÇÃO CORRETA de inserção (sem usar o sort()).
# No final, mostre a LISTA ORDENADA na tela.

'''lista = []   # MEU CÓDIGO
maior_num = 0
menor_num = 0
for valor in range(5):
    num = int(input('Digite um número: '))
    if num > maior_num:
        maior_num = num
        lista.append(maior_num)
        print('Adicionado no final da lista')
print(lista) '''


lista = []     # CÓDIGO GUANABARA
for v in range(0 ,5):
    n = int(input(f'Digite o {v+1}° valor: '))
    if v == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')