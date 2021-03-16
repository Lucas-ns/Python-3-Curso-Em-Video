from datetime import date
individuo = {}
individuo['nome'] = str(input('Nome: '))
individuo['idade'] = date.today().year - int(input('Ano de Nascimento: '))
individuo['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if individuo['ctps'] != 0:
    individuo['contratação'] = int(input('Ano de Contratação: '))
    individuo['aposentadoria'] = (individuo['idade'] + ((individuo['contratação'] + 35) - date.today().year))
    individuo['salário'] = float(input('Salário: R$'))
print('-=' * 30)
for k, v in individuo.items():
    print(f'  - {k} tem o valor {v}')
