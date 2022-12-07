cont =  homem = mulher = 0
user = ''
while user in 'S':
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Sexo [M/F]: '))
    user = str(input('Quer continuar? [S/N]: '))
    if idade >= 18:
        cont += 1
    if sexo == 'M':
        homem += 1
    if sexo ==  'F' and idade < 20:
        mulher += 1
print('-=' * 20)
print(f'{cont} pessoas tem mais de 18 anos.')
print(f'Foram cadastrados {homem} homens.')
print(f'E {mulher} mulheres com menos de 18 anos')
