from random import randint
from time import sleep

print('-' * 20)
print('JOGA NA MEGA SENA')
print('-' * 20)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print()
print('-=' * 5, f'SORTEANDO {jogos} JOGOS', '=-' * 5)
print()
sorteados = []
lista = []
for j in range(1, jogos+1):
    while len(lista) != 7:
        r = randint(1, 60)
        if r not in lista:
            lista.append(r)
    lista.sort()
    sorteados.append(lista[:])
    lista.clear()
for i, s in enumerate(sorteados):
    sleep(1)
    print(f'Jogo {i+1}: {s}')
print()
print('-=' * 5, f'< BOA SORTE! >', '=-' * 5)
