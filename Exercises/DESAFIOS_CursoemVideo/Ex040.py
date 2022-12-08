nome = str(input('Digite o nome do aluno: '))
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Aluno {} está...[REPROVADO] '.format(nome))
    print('Média de: {}'.format(media))
elif media == 5 or media <= 6.9:
    print('Aluno {} está em...[RECUPERAÇÃO] '.format(nome))
    print('Média de: {}'.format(media))
else:
    print('O aluno {} está...[APROVADO] '.format(nome))
    print('Média de: {}'.format(media))

