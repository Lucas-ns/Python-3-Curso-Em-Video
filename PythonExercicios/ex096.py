def área(h, b):
    a = h * b
    print(f'A área de um terreno {h}x{b} é de {a}m²!')


print('Controle de Terrenos')
print('-' * 20)
área(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))
