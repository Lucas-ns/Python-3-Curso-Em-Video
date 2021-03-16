title = 'LOJA SUPER BARATÃO'
ending = ' FIM DO PROGRAMA '
print('-' * 30)
print(f'{title:^30}')
print('-' * 30)
soma = cont = menor = controlador = 0
mais_barato = ''
while True:
    produto = str(input('Nome do Produto: ').strip())
    preço = float(input('Preço: R$').strip())
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print('-' * 30)
    soma += preço
    controlador += 1
    if preço > 1000:
        cont += 1
    if controlador == 1 or preço < menor:
        menor = preço
        mais_barato = produto
    if res == 'N':
        break
print(f'{ending:-^40}')
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {cont} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {mais_barato} que custa R${menor}')
