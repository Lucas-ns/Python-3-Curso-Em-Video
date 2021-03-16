nome = input('Qual o seu nome? ')
if nome == 'Lucas':
    print('Que nome bonito!')
elif nome in 'Ana Matheus Pedro':
    print('Seu nome é popular no Brasil!')
else:
    print('Que nome normal..')
print('Tenha um bom dia, {}!'.format(nome))