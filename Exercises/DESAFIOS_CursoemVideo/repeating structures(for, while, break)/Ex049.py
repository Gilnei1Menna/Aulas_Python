num = int(input('\033[1mDigite um número: \033[m'))
print(f'\033[1;33mTABUADA DO:\033[m \033[1;31m{num}\033[m')
for c in range(0, 11):
    print(f'\033[1;4m{num} x {c} = {num * c}\033[m')