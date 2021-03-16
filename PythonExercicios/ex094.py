from operator import itemgetter
geral = []
s_idade = []
pessoa = {}
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while pessoa['sexo'] != 'M' and pessoa['sexo'] != 'F':
        print('ERRO! Responda apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    s_idade.append(pessoa['idade'])
    res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while res != 'S' and res != 'N':
        print('ERRO! Responda apenas S ou N.')
        res = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    geral.append(pessoa.copy())
    if res in 'N':
        break
média = (sum(s_idade) / len(geral))
print('-=' * 30)
print(f'A) Ao todo temos {len(geral)} cadastradas.')
print(f'B) A média de idade é de {média:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in geral:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média:')
for p in geral:
    if p['idade'] >= média:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
