import emoji
from random import randint
from time import sleep
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
computador = randint(0, 2)
if jogador != 0 and jogador != 1 and jogador != 2:
    print('Jogada Inválida! Tente as opções acima!')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')

    print('-=' * 15)
    if computador == 0:
        print(emoji.emojize('Computador jogou Pedra :punch:', use_aliases=True))
    elif computador == 1:
        print(emoji.emojize('Computador jogou Papel :wave:', use_aliases=True))
    elif computador == 2:
        print(emoji.emojize('Computador jogou Tesoura :v:', use_aliases=True))

    if jogador == 0:
        print(emoji.emojize('Jogador jogou Pedra :punch:', use_aliases=True))
    elif jogador == 1:
        print(emoji.emojize('Jogador jogou Papel :wave:', use_aliases=True))
    elif jogador == 2:
        print(emoji.emojize('Jogador jogou Tesoura :v:', use_aliases=True))
    print('-=' * 15)

    if jogador == 0 and computador == 2:
        print('JOGADOR VENCE')
    elif jogador == 1 and computador == 0:
        print('JOGADOR VENCE')
    elif jogador == 2 and computador == 1:
        print('JOGADOR VENCE')
    elif computador == 0 and jogador == 2:
        print('COMPUTADOR VENCE')
    elif computador == 1 and jogador == 0:
        print('COMPUTADOR VENCE')
    elif computador == 2 and jogador == 1:
        print('COMPUTADOR VENCE')
    else:
        print('EMPATE')
