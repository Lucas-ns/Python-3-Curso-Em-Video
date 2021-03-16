número = int(input('Digite um número para ver sua tabuada: '))
for n in range(1, 11):
    print('{} x {:2} = {}'.format(número, n, número*n))
