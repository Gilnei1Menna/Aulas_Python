num = []
while True:
    num.append(int(input('Digite um número: ')))
    pergunta = str(input('Quer continuar? ')).upper()
    if pergunta not in 'S':
        break

pares = []
impares = []
for i, v in enumerate(num):  # estou colocando o valor NUM em V e nomeando como I,
                             # assim posso usar a variável na sequencia do meu código.
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'A lista completa é: {num}')
print(f'Os números pares são {pares}')
print(f'Os números impares são {impares}')
