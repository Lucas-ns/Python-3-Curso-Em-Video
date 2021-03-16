from random import randint
from time import sleep

def sorteia(lista):
    cont = 0
    print('Sorteando os 5 valores da lista: ', end='')
    while cont <= 4:
        lista.append(randint(1, 10))
        cont += 1
    for n in números:
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    s = 0
    for n in lista:
        if n % 2 == 0:
            s += n
    print(f'Somando os valores pares de {números}, temos um total de {s}.')


números = list()
sorteia(números)
somaPar(números)
