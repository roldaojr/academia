import sys
import inspect
from math import log10


def densidade2gordura(densidade, pessoa):
    if pessoa.idade >= 20:
        if pessoa.sexo == 1:
            return 495 / densidade - 450
        else:
            return 503 / densidade - 459
    elif pessoa.idade >= 17:
        if pessoa.sexo == 1:
            return 498 / densidade - 453
        else:
            return 505 / densidade - 462
    elif pessoa.idade >= 15:
        if pessoa.sexo == 1:
            return 503 / densidade - 459
        else:
            return 507 / densidade - 464
    elif pessoa.idade >= 13:
        if pessoa.sexo == 1:
            return 507 / densidade - 464
        else:
            return 512 / densidade - 469
    elif pessoa.idade >= 11:
        if pessoa.sexo == 1:
            return 523 / densidade - 481
        else:
            return 525 / densidade - 484
    elif pessoa.idade >= 9:
        if pessoa.sexo == 1:
            return 530 / densidade - 489
        else:
            return 535 / densidade - 495
    else:
        if pessoa.sexo == 1:
            return 538 / densidade - 497
        else:
            return 543 / densidade - 503


def percent_gordura_calc(nome, dobras):
    def decorated(func):
        func.metodo_gordura = True
        func.nome = nome
        func.dobras = dobras
        return func
    return decorated


# Ambos os sexos
@percent_gordura_calc('Pollock, Schmidt e Jackson 1980 (adultos)', (
    'tricepes', 'suprailiaca', 'coxa'))
def pollock_schmidt_jackson_1980(dobras, pessoa):
    soma = dobras.tricipes + dobras.suprailiaca + dobras.coxa
    if pessoa.sexo == 2:
        densidade = 1.0994921 - 0.0009929 * soma + 0.0000023 * (soma ** 2) - \
            0.0001392 * pessoa.idade
    else:
        densidade = 1.10938 - 0.0008267 * soma + 0.0000016 * (soma ** 2) - \
            0.0002574 * pessoa.idade
    return densidade2gordura(densidade, pessoa)


@percent_gordura_calc('Jackson & Pollock 1984 (homens, 18 a 61 anos)', (
    'toracica', 'abdominal', 'coxa'))
def jackson_pollock_1978(dobras, pessoa):
    soma = dobras.toracica + dobras.abdominal + dobras.coxa
    densidade = 1.1866 + 0.03049 * log10(soma) - 0.00027 * pessoa.idade
    return densidade2gordura(densidade, pessoa)


@percent_gordura_calc('Deurenberg et ali 1990 (meninos e meninas)', (
    'bicipes', 'tricipes', 'subescapular', 'suprailiaca'))
def deurenberg_et_al_1990(dobras, pessoa):
    soma = dobras.bicipes + dobras.tricipes + dobras.subescapular + dobras.suprailiaca
    if pessoa.sexo == 1:
        return 18.7 * log10(soma) - 11.91
    else:
        return 21.94 * log10(soma) - 18.89


@percent_gordura_calc('Boleau et ali 1985 (meninos e meninas)', (
    'tricipes', 'subescapular'))
def boleau_et_al_1985(dobras, pessoa):
    soma = dobras.tricipes + dobras.subescapular
    if pessoa.sexo == 1:
        return 1.35 * soma - 0.012 * (soma ** 2) - 4.4
    else:
        return 1.35 * soma - 0.012 * (soma ** 2) - 2.4


@percent_gordura_calc('Durnin & Rahman 1967 (adolescentes)', (
    'tricipes', 'bicipes', 'subescapular', 'suprailiaca'))
def durnin_rahman_1967_adolescente(dobras, pessoa):
    soma = dobras.tricipes + dobras.bicipes + dobras.subescapular + dobras.suprailiaca
    if pessoa.sexo == 1:
        densidade = 1.1533 - 0.0643 * log10(soma)
    else:
        densidade = 1.1369 - 0.0598 * log10(soma)
    return densidade2gordura(densidade, pessoa)


@percent_gordura_calc('Durnin & Rahman 1967 (jovens)', (
    'tricipes', 'bicipes', 'subescapular', 'suprailiaca'))
def durnin_rahman_1967_homem_jovem(dobras, pessoa):
    soma = dobras.tricipes + dobras.bicipes + dobras.subescapular + dobras.suprailiaca
    if pessoa.sexo == 1:
        densidade = 1.161 - 0.0632 * log10(soma)
    else:
        densidade = 1.1581 - 0.072 * log10(soma)
    return densidade2gordura(densidade, pessoa)


@percent_gordura_calc('Nagamine & Suzuki 1964 (japoneses de 18 a 27 anos)', (
    'tricipes', 'subescapular'))
def nagamine_suzuki_1967(dobras, pessoa):
    soma = dobras.tricipes + dobras.subescapular
    if pessoa.sexo == 1:
        densidade = 1.9013 - 0.00116 * soma
    else:
        densidade = 1.0897 - 0.00133 * soma
    return densidade2gordura(densidade, pessoa)


# Mulheres
@percent_gordura_calc('Jackson, Pollock e Ward 1980 (mulheres, 18 a 55 anos)', (
    'toracica', 'axilarmedia', 'tricipes', 'subescapular', 'abdominal',
    'suprailiaca', 'coxa'))
def jackson_pollock_ward_1980(dobras, pessoa):
    soma = dobras.toracica + dobras.axilarmedia + dobras.tricipes + \
        dobras.subescapular + dobras.abdominal + dobras.suprailiaca + \
        dobras.coxa
    densidade = 1.097 - 0.00046971 * soma + 0.00000056 * (soma ** 2) - \
        0.00012828 * pessoa.idade
    return densidade2gordura(densidade, pessoa)


@percent_gordura_calc('Petroski 1995 (mulheres, 18 a 61 anos)', (
    'axilarmedia', 'suprailiaca', 'coxa', 'panturrilhamedia'))
def petroski_1995_mulher(dobras, pessoa):
    soma = dobras.axilarmedia + dobras.suprailiaca + dobras.coxa + \
        dobras.panturrilhamedia
    densidade = 1.1954713 - 0.07513507 * log10(soma) - \
        0.00041072 * pessoa.idade
    return densidade2gordura(densidade, pessoa)


@percent_gordura_calc('Slaughter et ali 1988 (meninas brancas ou negras, dobras <= 35mm)', (
    'tricipes', 'subescapular'))
def slaugter_et_al_1988_meninas(dobras, pessoa):
    soma = dobras.tricipes + dobras.subescapular
    return 1.33 * soma - 0.13 * (soma ** 2) - 2


@percent_gordura_calc('Slaughter et ali 1988 (meninas brancas ou negras, dobras > 35mm)', (
    'tricipes', 'subescapular'))
def slaugter_et_al_1988_meninas_2(dobras, pessoa):
    soma = dobras.tricipes + dobras.subescapular
    return 0.546 * soma + 9.7


@percent_gordura_calc('Slaughter et ali 1988 (meninas brancas ou negras)', (
    'tricipes', 'subescapular'))
def slaugter_et_al_1988_meninas_3(dobras, pessoa):
    soma = dobras.tricipes + dobras.subescapular
    return 1.33 * soma - 0.13 * (soma ** 2) - 2


@percent_gordura_calc('Guedes 1995 (mulheres, estudantes universitárias)', (
    'coxa', 'suprailiaca', 'subescapular'))
def guedes_1995_mulher(dobras, pessoa):
    soma = dobras.coxa + dobras.suprailiaca + dobras.subescapular
    densidade = 1.1665 - 0.0706 * log10(soma)
    return densidade2gordura(densidade, pessoa)


@percent_gordura_calc('Pariskova 1961 (meninas brancas ou negras, 9 a 16 anos)', (
    'tricipes', 'subescapular'))
def pariskova_1961(dobras, pessoa):
    if pessoa.idade < 13:
        return 1.088 - 0.014 * log10(dobras.tricipes) - 0.036 * log10(dobras.subescapular)
    else:
        return 1.114 - 0.031 * log10(dobras.tricipes) - 0.041 * log10(dobras.subescapular)


@percent_gordura_calc('Katch & McArdle 1973 (mulheres, estudantes universitários)', (
    'tricipes', 'subescapular', 'coxa'))
def katch_mcardle_1973_mulher(dobras, pessoa):
    densidade = 1.08347 - 0.0006 * dobras.tricipes - \
        0.00151 * dobras.subescapular - 0.00097 * dobras.coxa
    return densidade2gordura(densidade, pessoa)


@percent_gordura_calc('Pollock et ali 1976 (mulheres jovens)', (
    'suprailiaca', 'coxa'))
def pollock_et_al_mulher_jovem(dobras, pessoa):
    densidade = 1.052 - 0.0008 * dobras.toracica - 0.0011 * dobras.coxa
    return densidade2gordura(densidade, pessoa)


@percent_gordura_calc('Durnin & Womersley 1974 (mulhers, 16 a 68 anos)', (
    'tricipes', 'bicipes', 'subescapular', 'suprailiaca'))
def durnin_womersley_1974_mulher(dobras, pessoa):
    soma = dobras.tricipes + dobras.bicipes + dobras.subescapular + dobras.suprailiaca
    if pessoa.idade < 20:
        densidade = 1.1549 - 0.0678 * log10(soma)
    elif pessoa.idade < 30:
        densidade = 1.1599 - 0.0717 * log10(soma)
    elif pessoa.idade < 40:
        densidade = 1.1423 - 0.0632 * log10(soma)
    elif pessoa.idade < 50:
        densidade = 1.1333 - 0.0612 * log10(soma)
    else:
        densidade = 1.1339 - 0.0645 * log10(soma)
    return densidade2gordura(densidade, pessoa)


@percent_gordura_calc('Sloan 1967 (mulheres, estudantes universitárias de 17 a 25 anos)', (
    'suprailiaca', 'tricepes'))
def sloan_1967_mulher(dobras, pessoa):
    densidade = 1.0764 - 0.00081 * dobras.suprailiaca - 0.00088 * dobras.tricepes
    return densidade2gordura(densidade, pessoa)


@percent_gordura_calc('Wilmore & Behnke 1969 (mulheres, estudantes universitários de 18 a 48 anos)', (
    'subescapular', 'tricipes', 'coxa'))
def wilmore_behnke_mulher(dobras, pessoa):
    densidade = 1.06234 - 0.00068 * dobras.subescapular - \
        0.00039 * dobras.tricipes - 0.00025 * dobras.coxa
    return densidade2gordura(densidade, pessoa)


# Homens
@percent_gordura_calc('Jackson, Pollock & Ward 1984 (homens)', (
    'toracica', 'axilarmedia', 'tricipes', 'subescapular',
    'abdominal', 'suprailiaca', 'coxa'))
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


@percent_gordura_calc('Petroski 1995 (homens, 18 a 61 anos)', (
    'subescapular', 'tricipes', 'suprailiaca', 'panturrilhamedia'))
def petroski_1995_homem(dobras, pessoa):
    soma = dobras.subescapular + dobras.tricipes + dobras.suprailiaca + \
        dobras.panturrilhamedia
    densidade = 1.10726863 - 0.00081201 * soma + 0.00000212 * (soma ** 2) - \
        0.00041761 * pessoa.idade
    return densidade2gordura(densidade, pessoa)


@percent_gordura_calc('Slaughter et ali 1988 (meminos brancos, dobras <= 35mm)', (
    'tricipes', 'subescapular'))
def slaugter_et_al_1988_brancos(dobras, pessoa):
    soma = dobras.tricipes + dobras.subescapular
    return 1.21 * soma - 0.008 * (soma ** 2) - 3.4


@percent_gordura_calc('Slaughter et ali 1988 (meninos negros, dobras <= 35mm)', (
    'tricipes', 'subescapular'))
def slaugter_et_al_1988_negros(dobras, pessoa):
    soma = dobras.tricipes + dobras.subescapular
    return 1.21 * soma - 0.008 * (soma ** 2) - 5.2


@percent_gordura_calc('Slaughter et ali 1988 (meninos brancos e negros, dobras > 35mm)', (
    'tricipes', 'subescapular'))
def slaugter_et_al_1988_brancos_e_negros_2(dobras, pessoa):
    return 0.783 * (dobras.tricipes + dobras.subescapular) + 1.6


@percent_gordura_calc('Slaughter et ali 1988 (meninos brancos e negros)', (
    'tricipes', 'panturrilhamedia'))
def slaugter_et_al_1988_brancos_e_negros(dobras, pessoa):
    return 0.735 * (dobras.tricipes + dobras.panturrilhamedia) + 1


@percent_gordura_calc('Guedes 1995 (homens, estudantes universitários)', (
    'tricipes', 'suprailiaca', 'abdominal'))
def guedes_1995_homem(dobras, pessoa):
    soma = dobras.tricipes + dobras.suprailiaca + dobras.abdominal
    densidade = 1.1714 - 0.0671 * log10(soma)
    return densidade2gordura(densidade, pessoa)


@percent_gordura_calc('Katch & McArdle 1973 (homens, estudantes universitários)', (
    'tricipes', 'subescapular', 'abdominal'))
def katch_mcardle_1973(dobras, pessoa):
    densidade = 1.09665 - 0.00103 * dobras.tricipes - \
        0.00056 * dobras.subescapular - \
        0.00054 * dobras.abdominal
    return densidade2gordura(densidade, pessoa)


@percent_gordura_calc('Pollock et ali 1976 (homens jovens)', (
    'toracica', 'coxa'))
def pollock_et_al_homem_jovem(dobras, pessoa):
    densidade = 1.09478 - 0.00103 * dobras.toracica - 0.00085 * dobras.coxa
    return densidade2gordura(densidade, pessoa)


@percent_gordura_calc('Pollock et ali 1976 (homens de meia-idade)', (
    'toracica', 'axilarmedia'))
def pollock_et_al_homem_meia_idade(dobras, pessoa):
    densidade = 1.0766 - 0.00098 * dobras.toracica - 0.00053 * dobras.axilarmedia
    return densidade2gordura(densidade, pessoa)


@percent_gordura_calc('Durnin & Womersley 1974 (homens, 17 a 72 anos)', (
    'tricipes', 'bicipes', 'subescapular', 'suprailiaca'))
def durnin_womersley_1974_homem(dobras, pessoa):
    soma = dobras.tricipes + dobras.bicipes + dobras.subescapular + dobras.suprailiaca
    if pessoa.idade < 20:
        densidade = 1.162 - 0.063 * log10(soma)
    elif pessoa.idade < 30:
        densidade = 1.1631 - 0.0632 * log10(soma)
    elif pessoa.idade < 40:
        densidade = 1.1422 - 0.0544 * log10(soma)
    elif pessoa.idade < 50:
        densidade = 1.162 - 0.07 * log10(soma)
    else:
        densidade = 1.1715 - 0.0779 * log10(soma)
    return densidade2gordura(densidade, pessoa)


@percent_gordura_calc('Sloan 1967 (homens, estudantes universitários de 18 a 26 anos)', (
    'coxa', 'subescapular'))
def sloan_1967(dobras, pessoa):
    densidade = 1.1043 - 0.001327 * dobras.coxa - 0.00131 * dobras.subescapular
    return densidade2gordura(densidade, pessoa)


@percent_gordura_calc('Wilmore & Behnke 1969 (homens, estudantes universitários de 17 a 37 anos)', (
    'abdominal', 'coxa'))
def wilmore_behnke(dobras, pessoa):
    densidade = 1.08543 - 0.000886 * dobras.abdominal - 0.00004 * dobras.coxa
    return densidade2gordura(densidade, pessoa)


formulas = [
    f for n, f in inspect.getmembers(sys.modules[__name__])
    if hasattr(f, 'metodo_gordura')
]
