l = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
area = l * h
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(l, h, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
