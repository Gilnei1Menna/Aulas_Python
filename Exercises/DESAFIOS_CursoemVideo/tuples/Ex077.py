palavras = ('Proposito', 'Programar', 'Trabalho', 'Dinheiro', 'Vida', 'Computador', 'Jogos', 'Corrida')
for p in palavras:
    print(f'\nNa palavra {p.upper()} tem as vogais: ', end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')

