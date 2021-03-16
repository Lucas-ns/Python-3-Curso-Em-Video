média = 0
idademaisvelho = 0
nomemaisvelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('-' * 10, '{}ª PESSOA'.format(p), '-' * 10)
    nome = str(input('Nome: ').strip())
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').strip())
    média = (média*(p-1)+idade)/p
    if p == 1 and sexo in 'Mm':
        idademaisvelho = idade
        nomemaisvelho = nome
    if idade > idademaisvelho and sexo in 'Mm':
        idademaisvelho = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
print('A média de idade do grupo é de {}'.format(média))
print('A idade do homem mais velho é {} e se chama {}.'.format(idademaisvelho, nomemaisvelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))