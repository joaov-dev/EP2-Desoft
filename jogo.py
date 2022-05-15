## Imports necessarios para o desenvolvimento:
from funcoes import *
from base_paises_normalizado import *
import dicas

## Variaveis:
EARTH_RADIUS = 6371
tentativas = 20
listaTentivas = []
listaChutes = []
mostraChutes = []
continuaJogo = True

vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'
reset = "\033[0;0m"

coresUsadas = []
coresSorteadas = []

paisSorteado = sorteia_pais(dic_normalizado)
entraPais = input('Escolha um pais para comecar: ')

while continuaJogo == True:
    while entraPais != paisSorteado:
        if entraPais == 'dica':
            print('----------------------------------------')
            print('1. Cor da Bandeira  - Custa 4 tentativas')
            print('2. Letra da Capital - Custa 3 tentativas')
            print('3. Area             - Custa 6 tentativas')
            print('4. Populacao        - Custa 5 tentativas')
            print('5. Continente       - Custa 7 tentativas')
            print('0. Sem dica')
            print('----------------------------------------')

            dicaEscolhida = input('Escolha sua opcao [0|1|2|3|4|5]: ')
            respostaDica = dicas.compraDicas(dicaEscolhida, paisSorteado, tentativas)
            print(respostaDica[0])

            if dicaEscolhida == '1':
                coresUsadas.append(respostaDica[0])
                coresSorteadas = respostaDica[2]

            tentativas -= respostaDica[1]

            print('Voce tem {} tentativas restantes!'.format(tentativas))
            entraPais = input('Escolha mais um pais: ')
        else:
            if entraPais in dic_normalizado.keys():
                if entraPais not in listaChutes:
                    if tentativas > 0:
                        dist = haversine(EARTH_RADIUS, dic_normalizado[paisSorteado]['geo']['latitude'], dic_normalizado[paisSorteado]['geo']['longitude'],dic_normalizado[entraPais]['geo']['latitude'], dic_normalizado[entraPais]['geo']['longitude'])
                        adiciona_em_ordem(entraPais, dist, listaTentivas)
                        listaChutes.append(entraPais)

                        mostraChutes = adiciona_em_ordem(entraPais, dist, mostraChutes)

                        print('\nErrou, o pais secreto esta a: {:.2f}'.format(dist))

                        print('\nInformacoes adquiridas: ')
                        print('--------------------------------- ')
                        for item in mostraChutes:
                            if item[1] <= 5000:
                                print(verde + '{} --> {:.2f}'.format(item[0], item[1]))
                            if item[1] > 5000 and item[1] <= 12500:
                                print(azul + '{} --> {:.2f}'.format(item[0], item[1]))
                            if item[1] > 12500:
                                print(vermelho + '{} --> {:.2f}'.format(item[0], item[1]))
                        print(reset + '--------------------------------- ')                    

                        tentativas -= 1
                        print('\nVoce tem {} tentativas restantes!'.format(tentativas))

                        entraPais = input('Escolha mais um pais: ')
                        
                    else:
                        print('\nVoce perdeu! o pais secreto era: {0}'.format(paisSorteado))
                        break

                else:
                    print('\nVoce ja chutou esse pais!')

                    entraPais = input('Escolha outro pais: ')
            else:
                print('\nEste pais nao existe, ou nao esta em nosso banco de dados!')
                
                entraPais = input('Escolha mais um pais: ')

    if entraPais == paisSorteado:
        print('\nVoce acertou! o pais era: {} '.format(paisSorteado))

        jogarNovamente = input('Deseja jogar novamente? [s | n]: ')
        if jogarNovamente == 's':
            
            tentativas = 20
            listaTentivas = []
            listaChutes = []
            paisSorteado = sorteia_pais(dic_normalizado)
            entraPais = input('\nEscolha um pais: ')

        elif jogarNovamente == 'n':
            print('Obrigado por jogar!')
            continuaJogo = False

        else:
            print('Resposta invalida, tente novamente.')
            jogarNovamente = input('Deseja jogar novamente? [s | n]: ')