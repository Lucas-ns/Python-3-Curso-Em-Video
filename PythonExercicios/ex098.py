from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} contando de {passo} em {passo}')
    sleep(1)
    if fim > inicio:
        for n in range(inicio, fim + 1, passo):
            print(f'{n} ', end='', flush=True)
            sleep(0.5)
        print('FIM!')
    else:
        if fim == 0:
            for n in range(inicio, fim - 1, - passo):
                sleep(0.5)
                print(f'{n} ', end='')
            print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)
