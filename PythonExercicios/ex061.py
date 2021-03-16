print('-=' * 10)
print('Gerador de PA')
print('-=' * 10)
número = int(input('Primeiro valor: '))
razão = int(input('Razão da PA: '))
cont = 0
while cont < 10:
    print('{} '.format(número), end='-> ')
    número += razão
    cont += 1
print('FIM')