from datetime import date
ano = int(input('Ano de nascimento: '))
sexo = str(input('Qual seu sexo (M ou F)? ')).upper()
ano_atual = (date.today().year)
alistamento = 18
idade = ano_atual - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, ano_atual))
if idade == alistamento and sexo == 'M':
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade > alistamento and sexo == 'M':
    print('Você já deveria ter se alistado há {} anos.\nSeu alistamento foi em {}.'.format((idade - alistamento), (ano + alistamento)))
elif idade < alistamento and sexo == 'M':
    print('Ainda faltam {} anos para o alistamento.\nSeu alistamento será em {}.'.format((alistamento - idade), (ano + alistamento)))
else:
    print('Mulheres não possuem alistamento obrigatório.')
