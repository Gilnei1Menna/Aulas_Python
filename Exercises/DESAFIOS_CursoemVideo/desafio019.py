import random
n1 = (input('Primeiro aluno: '))
n2 = (input('Sgundo aluno: '))
n3 = (input('Terceiro aluno: '))
n4 = (input('Quartop aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno selecionado foi {}'.format(escolhido))
