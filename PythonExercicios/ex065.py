res = 'S'
cont = média = soma = n = maior = menor = 0
while res != 'N':
    n = int(input('Digite um número: '))
    res = str(input('Quer continuar? [S/N] ').upper())
    soma += n
    cont += 1
    if maior > n:
        menor = n
    elif n > maior:
        maior = n
média = soma / cont
print('Você digitou {} números e a média foi {:.2f}.'.format(cont, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
