import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hip = math.hypot(co, ca)
print('O comprimento da hipotenusa é de {:.2f}.'.format(hip))

print("\n*************************************\n")#segunda maneira abaixo, sem o modulo.

co = float(input('Valor: '))
ca = float(input('Valor: '))
hip = (ca ** 2 + co ** 2) ** (1/2)
print(hip)
