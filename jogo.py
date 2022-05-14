## Imports necessarios para o desenvolvimento:
from funcoes import *
from base_paises_normalizado import *
import dicas

## Variaveis:
EARTH_RADIUS = 6371
tentativas = 20
listaTentivas = []
listaChutes = []
mostraChutes= []
continuaJogo = True

coresUsadas = []

paisSorteado = sorteia_pais(dic_normalizado)
entraPais = input('Escolha um pais para comecar: ')


while continuaJogo == True:
    while entraPais != paisSorteado:

        if:
            if entraPais in dic_normalizado.keys():
                if entraPais not in listaChutes:
                    if tentativas > 0:
                        dist = haversine(EARTH_RADIUS, dic_normalizado[paisSorteado]['geo']['latitude'], dic_normalizado[paisSorteado]['geo']['longitude'],dic_normalizado[entraPais]['geo']['latitude'], dic_normalizado[entraPais]['geo']['longitude'])
                        adiciona_em_ordem(entraPais, dist, listaTentivas)
                        listaChutes.append(entraPais)

                        mostraChutes = adiciona_em_ordem(entraPais, dist, mostraChutes)

                        print('\nErrou, o pais secreto esta a: {:.2f}'.format(dist))
