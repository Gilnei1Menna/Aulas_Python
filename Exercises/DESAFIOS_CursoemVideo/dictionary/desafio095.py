jogador = {}
galera = []
gols = []
while True:
  gols.clear()
  jogador.clear()
  jogador['nome'] = input('Nome: ')
  p = int(input('Partidas jogadas: '))
  for i in range (p):
    g = int(input(f'Gols na partida {i+1}: '))
    gols.append(g)
  jogador['gols'] = gols[:]
  jogador['total'] = sum(gols)
  galera.append(jogador.copy())
  d = input('Deseja continuar? ').lower()[0]
  if d != 's':
    break
print('=-'*30)
print('cod nome        gols        total')
for i, v in enumerate(galera):
  print('{:<4}'.format(i+1), end='')
  for k, valor in galera[i].items():
    print('{:<12}'.format(str(valor)), end='')
  print()
  
while True:
  print('=-'*30)
  x = int(input('Mostrar dados de qual jogador?(999 para) '))
  if x == 999:
    print('Programa finalizado')
    break
  elif x-1>len(galera):
    print('Este jogador não existe')
  else:
    print(f'Dados de {galera[x-1]["nome"]}:')
    for i in range (len(galera[x-1]['gols'])):
      print(f'=> na partida {i+1} fez {galera[x-1]["gols"][i]} gols.')