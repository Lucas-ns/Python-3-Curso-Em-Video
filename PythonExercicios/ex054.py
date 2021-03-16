from datetime import date
maiores = 0
menores = 0
ano_atual = date.today().year
for pess in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = ano_atual - ano
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print('\nAo todo tivemos {} pessoas maiores de idade'.format(maiores))
print('E também tivemos {} pessoas menores de idade'.format(menores))
