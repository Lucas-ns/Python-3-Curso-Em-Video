s = 0
cont = 0
for n in range(1, 7):
    número = int(input('Digite o {}º valor: '.format(n)))
    if número % 2 == 0:
        s += número
        cont += 1
if cont > 1:
    print('Você informou {} números PARES e a soma desses números é {}'.format(cont, s))
else:
    print('Você informou apenas {} número PAR e ele é o {}'.format(cont, s))
