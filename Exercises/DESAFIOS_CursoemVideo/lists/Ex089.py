lista = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    pergunta = str(input('Quer continuar? [S/N] ')).upper()[0]
    if pergunta != 'S':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":<8}')
print('-' * 26)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:<8.1f}')
while True:
    print('-' * 30)
    nota_aluno = int(input('Mostar notas de qual aluno? (999 [interrompe]): '))
    if nota_aluno == 999:
        print('FINALIZANDO...')
        break
    if nota_aluno <= len(lista) -1:
        print(f'Notas de {lista[nota_aluno][0]} são {lista[nota_aluno][1]}')