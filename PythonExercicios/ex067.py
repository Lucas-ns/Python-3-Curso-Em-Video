while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if num < 0:
        break
    tab = 1
    while tab <= 10:
        print(f'{num} x {tab} = {num * tab}')
        tab += 1
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
