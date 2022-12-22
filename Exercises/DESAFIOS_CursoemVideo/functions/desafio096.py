'''print(f'{"ÁREA DO TERRENO":^30}')
print('-' * 30)
largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))
area = largura * comprimento
print(f'A área do terreno de {largura}x{comprimento} é de {area}')'''


def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno de {larg}m x {comp}m é de {a} m²')


print(f'{"ÁREA DO TERRENO":^30}')
print('-' * 30)
l = float(input('Digite a largura do terreno: '))
c = float(input('Digite o comprimento do terreno: '))
area(l, c)