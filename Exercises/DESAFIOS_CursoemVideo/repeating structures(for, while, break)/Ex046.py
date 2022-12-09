from time import sleep
import emoji
print('\033[1;43m[Vamos iniciar a contagem de 10 segundos para os fogos]\033[m')
print('-'* 3)
sleep(2)
for c in range(10, 0, -1):
    sleep(1)
    print (f'\033[1;31m{c}\033[m')
print('\033[1;33mBOMM!!!\033[m 💥🎆💥🎆💥')