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
durnin_womersley_1974.dobras = (
    'tricipes', 'bicipes', 'subescapular', 'suprailiaca')


def jackson_pollock_ward_1980(dobras, pessoa):
    soma = dobras.toracica + dobras.axilarmedia + dobras.tricipes + \
           dobras.subescapular + dobras.abdominal + dobras.suprailiaca + \
           dobras.coxa
    densidade = 1.097 - 0.00046971 * soma + 0.00000056 * (soma**2) - \
                0.00012828 * pessoa.idade
    return densidade2gordura(densidade, pessoa)

jackson_pollock_ward_1980.nome = 'Jackson, Pollock e Ward 1980 (mulheres, 18 a 55 anos)'
jackson_pollock_ward_1980.dobras = (
    'toracica', 'axilarmedia', 'tricipes', 'subescapular',
    'abdominal', 'suprailiaca', 'coxa')


def pestroski_1995_mulher(dobras, pessoa):
    soma = dobras.axilarmedia + dobras.suprailiaca + dobras.coxa + \
           dobras.panturrilhamedia
    densidade = 1.1954713 - 0.07513507 * log10(soma) - \
                0.00041072 * pessoa.idade
    return densidade2gordura(densidade, pessoa)

pestroski_1995_mulher.nome = 'Pestroski 1995 (mulheres, 18 a 61 anos)'
pestroski_1995_mulher.dobras = (
    'axilarmedia', 'suprailiaca', 'coxa', 'panturrilhamedia')


def pollock_schimidt_jackson_1980(dobras, pessoa):
    soma = dobras.tricipes + dobras.suprailiaca + dobras.coxa
    if pessoa.sexo == 2:
        densidade = 1.0994921 - 0.0009929 * soma + 0.0000023 * (soma**2) - \
                    0.0001392 * pessoa.idade
    else:
        densidade = 1.10938 - 0.0008267 * soma + 0.0000016 * (soma**2) - \
                    0.0002574 * pessoa.idade
    return densidade2gordura(densidade, pessoa)

pollock_schimidt_jackson_1980.nome = 'Pollock, Schimidt e Jackson 1980 (adultos)'
pollock_schimidt_jackson_1980.dobras = (
    'tricepes', 'suprailiaca', 'coxa')


def jackson_pollock_1978(dobras, pessoa):
    soma = dobras.toracica + dobras.abdominal + dobras.coxa
    densidade = Decimal(0.03049) + Decimal(log10(soma)) - Decimal(0.00027) * \
                pessoa.idade
    return densidade2gordura(densidade, pessoa)

jackson_pollock_1978.nome = 'Jackson, Pollock 1984'
jackson_pollock_1978.dobras = ('toracica', 'abdominal', 'coxa')


def pestroski_1995_homem(dobras, pessoa):
    soma = dobras.subescapular + dobras.tricipes + dobras.suprailiaca + \
           dobras.panturrilhamedia
    densidade = 1.10726863 - 0.00081201 * soma + 0.00000212 * (soma**2) - \
                0.00041761 * pessoa.idade
    return densidade2gordura(densidade, pessoa)

pestroski_1995_homem.nome = 'Pestroski 1995 (homens, 18 a 61 anos)'
pestroski_1995_homem.dobras = (
    'subescapular', 'tricipes', 'suprailiaca', 'panturrilhamedia')


def jackson_pollock_ward_1984(dobras, pessoa):
    soma = dobras.toracica + dobras.axilarmedia + dobras.tricipes + \
           dobras.subescapular + dobras.abdominal + dobras.suprailiaca + \
           dobras.coxa
    if pessoa.sexo == 1:
        densidade = 1.112 - (0.00043499 * soma) + (0.00000055 * (soma ** 2)) - \
                    (0.00028826 * pessoa.idade)
    else:
        densidade = 1.097 - (0.00046971 * soma) + (0.00000056 * (soma ** 2)) - \
                    (0.00012828 * pessoa.idade)
    return densidade2gordura(densidade, pessoa)

jackson_pollock_ward_1984.nome = 'Jackson, Pollock e Ward 1984'
jackson_pollock_ward_1984.dobras = (
    'toracica', 'axilarmedia', 'tricipes', 'subescapular',
    'abdominal', 'suprailiaca', 'coxa')

formulas = (
    durnin_womersley_1974, jackson_pollock_1978, jackson_pollock_ward_1980,
    jackson_pollock_ward_1984, pestroski_1995_homem, pestroski_1995_mulher,
    pollock_schimidt_jackson_1980)
