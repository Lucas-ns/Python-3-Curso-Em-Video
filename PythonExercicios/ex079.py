list = []
res = ''
while res != 'N':
    value = int(input('Digite um valor: '))
    if value not in list:
        list.append(value)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while res != 'S' and res != 'N':
        res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('-=' * 30)
print(f'Você digitou os valores {sorted(list)}')
