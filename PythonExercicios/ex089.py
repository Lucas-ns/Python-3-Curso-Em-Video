lista = []
ficha = []
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Nota 1: ')))
    lista.append(float(input('Nota 2: ')))
    lista.append((lista[1]+lista[2]) / 2)
    ficha.append(lista[:])
    lista.clear()
    res = str(input('Quer continuar? [S/N] '))
    if res in 'Nn':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[3]:>8.1f}')
while True:
    print('-' * 26)
    opção = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opção == 999:
        print('FINALIZANDO...')
        break
    if opção <= len(ficha) - 1:
        print(f'As notas de {ficha[opção][0]} são {ficha[opção][1]} e {ficha[opção][2]}')
print('Volte Sempre')