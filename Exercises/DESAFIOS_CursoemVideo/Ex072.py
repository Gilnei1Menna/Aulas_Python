contagem = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente...', end='')
print(f'Você digitou o número {contagem[num]}')

# A condição WHILE faz um LOOP no código até a condição seja alcançada,
# no exemplo acima ele vai se repetir até que o IF seja verdadeiro e acione o BREAK, e
# então saia para o print que está fora do IF onde vai impimir o elemento da tupla, indicando a posição
# com um valor digitado na variavel NUM.