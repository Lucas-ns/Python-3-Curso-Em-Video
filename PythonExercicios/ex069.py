title = 'CADASTRE UMA PESSOA'
print('-' * 30)
print(f'{title:^30}')
print('-' * 30)
cont = quant_homens = quant_mulheres = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ').upper().strip())[0]
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Sexo: [M/F] ').upper().strip())[0]
    print('-' * 30)
    res = str(input('Quer continuar? [S/N] ').upper().strip())
    while res != 'S' and res != 'N':
        res = str(input('Quer continuar? [S/N] ').upper().strip())
    print('-' * 30)
    print(f'{title:^30}')
    print('-' * 30)
    if idade > 18:
        cont += 1
    if sexo == 'M':
        quant_homens += 1
    if idade < 18 and sexo == 'F':
        quant_mulheres += 1
    if res == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {cont}')
print(f'Ao todo temos {quant_homens} homens cadastrados')
print(f'E temos {quant_mulheres} mulheres com menos de 20 anos')
