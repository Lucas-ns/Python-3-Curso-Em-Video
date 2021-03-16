matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
s_coluna = s_par = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if l == 1:
            maior = matriz[1][0]
            if matriz[1][1] > maior:
                maior = matriz[1][1]
            if matriz[1][2] > maior:
                maior = matriz[1][2]
        if matriz[l][c] % 2 == 0:
            s_par += matriz[l][c]
        s_coluna += matriz[l][2]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma de todos os pares é {s_par}.')
print(f'A soma dos valores da 3ª coluna é {s_coluna}.')
print(f'O maior valor da 2ª linha é {maior}.')
print('-=' * 30)
