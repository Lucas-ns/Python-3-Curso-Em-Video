dado = list()
pessoas = list()
cont = maior_peso = menor_peso = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    esc = str(input('Quer continuar? [S/N] ')).upper().strip()
    if cont == 0:
        maior_peso = menor_peso = dado[1]
    else:
        if dado[1] > maior_peso:
            maior_peso = dado[1]
        if dado[1] < menor_peso:
            menor_peso = dado[1]
    cont += 1
    pessoas.append(dado[:])
    dado.clear()
    if esc in 'N':
        break
print(f'Ao todo, você cadastrou {cont} pessoas.')
print(f'O maior peso foi de {maior_peso:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menor_peso:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'[{p[0]}]', end='')
print()
