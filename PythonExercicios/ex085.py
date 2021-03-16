lista = [[], []]
valores = 0
for n in range(1, 8):
    valores = int(input(f'Digite o {n}º valor: '))
    if valores % 2 == 0:
        lista[0].append(valores)
    if valores % 2 == 1:
        lista[1].append(valores)
print('-=' * 50)
print(f'Os valores pares digitados foram: {sorted(lista[0])}')
print(f'Os valores ímpares digitados foram: {sorted(lista[1])}')
