"""teste = list()
teste.append('Lucas')
teste.append(21)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 34
galera.append(teste[:])
print(galera)"""

galera = [['Lucas', 21], ['Henrique', 22], ['Sara', 23], ['Mattheus', 21]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
