def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    boletim = {}
    boletim['total'] = len(n)
    boletim['maior'] = max(n)
    boletim['menor'] = min(n)
    boletim['média'] = 0
    boletim['média'] = sum(n) / len(n)
    if sit:
        if boletim['média'] > 7:
            boletim['situação'] = 'BOA'
        elif 7 >= boletim['média'] > 5:
            boletim['situação'] = 'RAZOÁVEL'
        else:
            boletim['situação'] = 'RUIM'
    return boletim


#programa principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
