nome = input('Digite seu nome completo: ')
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minuscúlas é {}'.format(nome.lower()))
print('O seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))