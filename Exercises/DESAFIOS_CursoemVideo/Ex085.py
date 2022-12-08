'''lista_comp = []
lista_par = par = []
lista_imp = []
for c in range(0, 7):
    lista_comp.append(int(input(f'Digite o {c + 1}° valor: ')))
for v in lista_comp:
    if v % 2 == 0:
        lista_par.append(v)
        lista_par.sort()
        print(f'Os valores pares digitados foram: {lista_par}')
    else:
        lista_imp.append(v)
        lista_imp.sort()
        print(f'Os valores impares digitados foram: {lista_imp}')'''

lista = [[], []]
for c in range(1, 8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
        lista[0].sort()
    else:
        lista[1].append(valor)
        lista[1].sort()

'''lista_final.append(lista_par)
lista_final.append(lista_imp)'''

print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')
print(f'A minha lista final com as duas listas é: {lista}')
