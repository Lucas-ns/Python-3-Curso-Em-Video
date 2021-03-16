cont = 0
num = int(input('Digite um número: '))
for c in range(1, num+1):
    if num % c == 0:
        cont += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\033[m\nO número {} foi divisível por {} vezes'.format(num, cont))
if cont == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
