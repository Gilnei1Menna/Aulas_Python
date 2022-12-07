lista_comp = [[], [[], []]]
# print(lista_comp[1][0])
nome = str(input('Digite o nome do aluno: '))
lista_comp[0].insert(0, nome)
lista_comp[1][0].append(int(input('Digite a primeira nota: ')))
lista_comp[1][1].append(int(input('Digite a segunda nota: ')))
print(lista_comp)