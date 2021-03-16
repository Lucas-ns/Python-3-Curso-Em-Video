salário = float(input('Qual é o salário do funcionário? R$'))
if salário > 1250:
    ajuste = (salário * 0.1) + salário
else:
    ajuste = (salário * 0.15) + salário
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, ajuste))
