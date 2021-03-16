from random import randint
print('Sou seu computador...')
print('Acabei de pensar em um número de 0 a 10.')
print('Será que você consegue adivinhar qual foi?')
palpites = 0
jogador = ''
computador = randint(0, 10)
while jogador != computador:
    jogador = int(input('Qual é seu palpite? '))
    if jogador < computador:
        print('Mais... Tente mais uma vez.')
    if jogador > computador:
        print('Menos... Tente mais uma vez.')
    palpites += 1
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
