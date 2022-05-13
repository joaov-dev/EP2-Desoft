## Imports necessarios para o desenvolvimento:
from funcoes import *
from base_paises_normalizado import *
import dicas

## Variaveis:
EARTH_RADIUS = 6371
tentativas = 20
listaTentivas = []
listaChutes = []
continuaJogo = True

coresUsadas = []

paisSorteado = sorteia_pais(dic_normalizado)
entraPais = input('Escolha um pais para comecar: ')



if entraPais in dic_normalizado.keys():
                if entraPais not in listaChutes:
                    if tentativas > 0:
                        dist = haversine(EARTH_RADIUS, dic_normalizado[paisSorteado]['geo']['latitude'], dic_normalizado[paisSorteado]['geo']['longitude'],dic_normalizado[entraPais]['geo']['latitude'], dic_normalizado[entraPais]['geo']['longitude'])
                        adiciona_em_ordem(entraPais, dist, listaTentivas)
                        listaChutes.append(entraPais)

                        print('Errou, o pais secreto esta a: {0}'.format(dist))

                        entraPais = input('Escolha mais um pais: ')
                        
                    else:
                        print('Voce perdeu! ')
                    
                    tentativas -= 1
                    print('Voce tem {} tentativas restantes!'.format(tentativas))

                else:
                    print('Voce ja chutou esse pais!')

                    entraPais = input('Escolha outro pais: ')
            else:
                print('Este pais nao existe, ou nao esta em nosso banco de dados!')
                
                entraPais = input('Escolha mais um pais: ')
