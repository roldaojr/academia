from math import log10
from decimal import Decimal


def densidade2gordura(densidade, pessoa):
    if pessoa.idade >= 20:
        if pessoa.sexo == 1:
            return 495/densidade - 450
        else:
            return 503/densidade - 459
    elif pessoa.idade >= 17: 
        if pessoa.sexo == 1:
            return 498/densidade - 453
        else:
            return 505/densidade - 462
    elif pessoa.idade >= 15:
        if pessoa.sexo == 1:
            return 503/densidade - 459
        else:
            return 507/densidade - 464
    elif pessoa.idade >= 13:
        if pessoa.sexo == 1:
            return 507/densidade - 464
        else:
            return 512/densidade - 469
    elif pessoa.idade >= 11:
        if pessoa.sexo == 1:
            return 523/densidade - 481
        else:
            return 525/densidade - 484
    elif pessoa.idade >= 9:
        if pessoa.sexo == 1:
            return 530/densidade - 489
        else:
            return 535/densidade - 495
    else:
        if pessoa.sexo == 1:
            return 538/densidade - 497
        else:
            return 543/densidade - 503


def durnin_womersley_1974(dobras, pessoa):
    soma = dobras.tricipes + dobras.bicipes + dobras.subescapular + dobras.suprailiaca
    if pessoa.sexo == 1:
        densidade = 1.1765 - 0.0744 * log10(soma)
    else:
        densidade = 1.1567 - 0.0717 * log10(soma)
    return densidade2gordura(densidade, pessoa)


durnin_womersley_1974.nome = 'Durnin Womersley 1974'


def jackson_pollock_ward_1984(dobras, pessoa):
    soma = dobras.toracica + dobras.axilarmedia + dobras.tricipes + \
           dobras.subescapular + dobras.abdominal + dobras.suprailiaca + dobras.coxa
    if pessoa.sexo == 1:
        print(type(soma), type(1.112), type(2))
        densidade = Decimal(1.112) - (Decimal(0.00043499) * soma) + \
                    (Decimal(0.00000055) * (soma ** 2)) - \
                    (Decimal(0.00028826) * pessoa.idade)
    else:
        densidade = Decimal(1.097) - (Decimal(0.00046971) * soma) + \
                    (Decimal(0.00000056) * (soma ** 2)) - \
                    (Decimal(0.00012828) * pessoa.idade)
    return densidade2gordura(densidade, pessoa)

jackson_pollock_ward_1984.nome = 'Jackson, Pollock e Ward 1984'

formulas = [durnin_womersley_1974, jackson_pollock_ward_1984]
