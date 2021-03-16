real = float(input('Digite o quanto de dinheiro você tem na carteira? R$'))
dólar = real / 5.31
euro = real / 6.28
print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dólar))
print('Com R${:.2f} você pode comprar €{:.2f}'.format(real, euro))