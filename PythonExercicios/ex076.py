print('-'*45)
print(f'{"LISTAGEM DE PREÇOS":^45}')
print('-'*45)
itens = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Caneta', 22.30,
         'Livros', 34.90)
for pos in range(0, len(itens)):
    if pos % 2 == 0:
        print(f'{itens[pos]:.<30}', end=' ')
    else:
        print(f'R${itens[pos]:>8.2f}')
print('-'*45)