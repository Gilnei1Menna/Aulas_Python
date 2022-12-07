import math
import random

print('Estou pensando um número... ')

print('[TENTE ADVINHAR]')
al = random.randint(0, 5)
num = int(input('Digite um número: '))
print('O número pensado foi {}'.format(al))
if num == al:
    print('[VOCÊ VENCEU]')
else:
    print('[VOCÊ PERDEU]')
