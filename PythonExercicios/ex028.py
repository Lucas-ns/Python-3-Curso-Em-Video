from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
user = int(input('Em que número eu pensei? '))
pc = randint(0, 5)
print('PROCESSANDO...')
sleep(2)
if user == pc:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(pc, user))
