print('=' * 50)
print('10 PRIMEIROS TERMOS DE UMA PA')
print('=' * 50)
número = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = número + (10 - 1) * razão
for c in range(número, décimo + razão, razão):
    print('{} '.format(c), end='-> ')
print('ACABOU!')
