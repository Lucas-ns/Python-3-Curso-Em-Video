sexo = str(input('Digite seu sexo: [M/F]').upper()[0].strip())
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ').upper()[0].strip())
print('Sexo {} registrado com sucesso!'.format(sexo))