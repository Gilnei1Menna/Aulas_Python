from random import randint
valor = comp = total = v = d = 0
while d == 0:
    valor = int(input('Diga um valor: '))
    comp = randint(0, 10)
    total = valor + comp
    parouimpar = str(input('Escolha par ou impar: [P/I] ')).upper()
    print('-=' * 15)
    if total % 2 == 0 and parouimpar == 'P':
        v += 1
    elif total % 2 != 0 and parouimpar == 'I':
        v += 1
    else:
        d += 1
        break
    print('[CONTINUAR...]')
print(f'Você jogou {valor} e o computador {comp} a soma é {total}', '[DEU PAR]' if total % 2 == 0 else '[DEU IMPAR]')
print(f'Você perdeu após ganhar {v} vezes. ')
