frase = str(input('Digite uma frase: ')).strip() # tira os espaços do inicio/final da frase
palavras = frase.split() # separa cada palavra da frase em uma string
junto = ''.join(palavras).upper() # substitui os espaços entre as strings
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(inverso)
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase diditada não é uma palindromo!')