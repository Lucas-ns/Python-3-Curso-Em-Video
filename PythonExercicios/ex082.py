lista = []
par = []
ímpar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    res = str(input('Quer continuar? [S/N] ')).strip()[0]
    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        ímpar.append(n)
    if res in 'Nn':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de pares é {ímpar}')
