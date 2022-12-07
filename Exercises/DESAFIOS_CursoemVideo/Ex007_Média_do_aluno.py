nome = input('Digite o nome do aluno: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print(f'A nota média do aluno(a) \033[4;30m{nome}\033[m, é \033[4;30m{(n1 + n2) / 2:.1f}')
