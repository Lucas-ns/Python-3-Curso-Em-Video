valor_casa = float(input('Qual é o valor da casa: R$'))
salário = float(input('Qual é salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = valor_casa / (anos * 12)
mínimo = salário * 0.30

print('Para pagar uma casa de R${:.2f} em {} anos,'.format(valor_casa, anos), end=' ')
print('a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
