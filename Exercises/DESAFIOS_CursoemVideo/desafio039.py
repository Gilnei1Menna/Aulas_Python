ano = int(input('Digite o ano de nascimento: '))
idade = 2022 - ano
if idade < 18:
    print('Você tem {} anos, e daqui a  {} anos vai ter que se apresentar ao serviço militar.'.format(idade, 18 - idade))
elif idade == 18:
    print('Você tem {} anos, e precisa se apresentar ao serviço militar imediatamente.'.format(idade))
else:
    print('Já passou do tempo do seu alistamento militar a {} anos.'.format(idade - 18))
    
