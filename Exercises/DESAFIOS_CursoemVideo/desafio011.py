lar = float(input('Informe a largura da parede: '))
alt = float(input('Informe a altura da parede: '))
area = lar * alt
print(f'A  parede possui \033[4m{area} m²\033[m e precisamos de \033[1;31;40m{area / 2}\033[m litros de tinta')
