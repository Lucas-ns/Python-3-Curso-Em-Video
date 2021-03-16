time = []
jogador = {}
gols = []
while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {p+1}? ')))
        jogador['gols'] = gols.copy()
        jogador['total'] = sum(gols)
    time.append(jogador.copy())
    jogador.clear()
    gols.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO Responda S ou N.')
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"cod":<4}{"nome":<15}{"gols":<15}{"total":>5}')
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    opc = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if opc == 999:
        break
    if opc >= len(time):
        print(f'ERRO! Jogador não encontrado com o código {opc}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[opc]["nome"]}')
        for i, g in enumerate(time[opc]['gols']):
            print(f'No jogo {i + 1} ele fez {g} gols.')
    print('-' * 40)
print('<< Encerrando >>')