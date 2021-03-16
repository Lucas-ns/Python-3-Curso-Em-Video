preco_antigo = float(input('Qual é o preço do produto? R$'))
preco_desc = preco_antigo - (preco_antigo * 0.05)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco_antigo, preco_desc))
