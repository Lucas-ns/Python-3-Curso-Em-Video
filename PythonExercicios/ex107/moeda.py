def aumentar(preço, taxa):
    preço += preço * (taxa/100)
    return preço


def diminuir(preço, taxa):
    preço -= preço * (taxa / 100)
    return preço


def dobro(preço):
    return preço * 2


def metade(preço):
    return preço / 2

