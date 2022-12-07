real = float(input('\033[1;30;41mQuanto  dineiro você tem na carteira?\033[m '))
dolar = real / 3.27
print('Com R$\033[4m{:.2f}\033[m você poderia comprar U$\033[4m{:.2f}\033[m em \033[4m2016!'.format(real, dolar))


