jogador = {}
gols = []
totgols = 0
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for p in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {p+1}? ')))
totgols = sum(gols)
jogador['gols'] = gols.copy()
jogador['total'] = totgols
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for p in range(0, partidas):
    print(f'    => Na partida {p+1}, fez {gols[p]} gols.')
print(f'Foi um total de {totgols} gols.')
