from random import *
from funcoes import *
from base_paises_normalizado import *

coresUsadas = []


def compraDicas(entrada, paisSorteado, tentativas, letrasUsadas):
    listaCores = []
    tentativasGastas = 0
    acabouCores = False

    if entrada == '1' and tentativas > 4:
        for cor, valor in dic_normalizado[paisSorteado]['bandeira'].items():
            if valor != 0 and cor != 'outras': 
                listaCores.append(cor)
        corSorteada = choice(listaCores)

        if corSorteada in coresUsadas:
            corSorteada = choice(listaCores)
        coresUsadas.append(corSorteada)
            
        if len(coresUsadas) == len(listaCores)-1:
            acabouCores = True
        

        tentativasGastas = 4
        return [corSorteada, tentativasGastas, acabouCores]
    
    if entrada == '2' and tentativas > 3:
        capital = dic_normalizado[paisSorteado]['capital']
        letraSorteada = sorteia_letra(capital, letrasUsadas)
        letrasUsadas.append(letraSorteada)

        tentativasGastas = 3
        return [letraSorteada, tentativasGastas]

    if entrada == '3' and tentativas > 6:
        area = dic_normalizado[paisSorteado]['area']

        tentativasGastas = 6
        return [area, tentativasGastas]

    if entrada == '4' and tentativas > 5:
        pop = dic_normalizado[paisSorteado]['populacao']

        tentativasGastas = 5
        return [pop, tentativasGastas]
    
    if entrada == '5' and tentativas > 7:
        continente = dic_normalizado[paisSorteado]['continente']

        tentativasGastas = 7
        return [continente, tentativasGastas]