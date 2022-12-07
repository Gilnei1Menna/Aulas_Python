ano = int(input('Digite o ano de nascimento do atleta: '))
idade = 2022 - ano
if idade <= 9:
    print('''Você tem {} anos, sua categoria é:
[MIRIM]'''.format(idade))
elif idade <= 14:
    print('''Você tem {} anos, sua categoria é: 
[INFANTIL]'''.format(idade))
elif idade <= 19:
    print('''Você tem {} anos, sua categoria é:
[JUNIOR]'''.format(idade))
elif idade <= 20:
    print('''Você tm {} anos, sua categoria é:
[SENIOR]'''.format(idade))
else:
    print('''Você tem {} anos, sua categoria é:
[MASTER]'''.format(idade))