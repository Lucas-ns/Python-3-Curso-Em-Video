pesos = []
for pessoas in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(pessoas)))
    pesos += [peso]
print('O maior peso lido foi {}Kg'.format(max(pesos)))
print('O menor peso lido foi {}Kg'.format(min(pesos)))