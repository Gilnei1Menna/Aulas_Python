a_r = dict()
a_r['nome'] = str(input('Digite o nome do aluno: '))
a_r['média'] = float(input(f'Digite a média do aluno, {a_r["nome"]}: ')) 
if a_r['média'] >= 7:
    a_r['situação'] = '[APROVADO]'
else:
    a_r['situação'] = '[REPROVADO]'
print(f'O aluno, {a_r["nome"]}, está {a_r["situação"]}!')
