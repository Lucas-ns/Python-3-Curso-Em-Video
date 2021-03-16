soma = 0
cont = 0
for n in range(1, 501):
    if n % 3 == 0 and n % 2 == 1:
        cont += 1
        soma += n
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))