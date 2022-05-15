import math
import random

def haversine (r, p1, l1, p2, l2):
    p1_rad= math.radians(p1)
    p2_rad= math.radians(p2)
    l1_rad= math.radians(l1)
    l2_rad= math.radians(l2)

    
    d1= (math.sin((p2_rad-p1_rad)/2))**2
    d2= math.cos(p1_rad)
    d3= math.cos(p2_rad)
    d4= (math.sin((l2_rad- l1_rad)/2))**2
    dt= d1 + (d2*d3*d4)

    d= 2 * r * math.asin(dt**(1/2))

    return d



def normaliza(dic):
    d = {}
    for cont in dic:
        for pais in dic[cont]:
            d[pais] = dic[cont][pais]
            d[pais]['continente'] = cont
    return d


def sorteia_pais(dic):
    nl = []
    for pais in dic:
        nl.append(pais)

    return random.choice(nl)

def adiciona_em_ordem(nome, dist, lista):
    i = 0
    nl = [nome, dist]
    dist2 = 0
    for pais in lista:
        if pais[1] > dist2 and pais[1] < dist:
            dist2 = pais[1]
            i += 1

    if nl not in lista:
        lista.insert(i, nl)

    return lista

def esta_na_lista(nome, lista):
    nl = []
    for pais in lista:
        nl.append(pais[0])
    
    check = False
    if nome in nl:
        check = True
    
    return check

def sorteia_letra(palavra,lista):
    letrasDisponiveis = letras_totais(palavra, lista)
    if len(letrasDisponiveis) == 0:
        return ""
    else:
        letraAleatoria = random.choice(letrasDisponiveis)
        return letraAleatoria


def letras_totais(palavra, lista):
        cEspecial = ['.', ',', '-', ';', ' ']
        letrasDisponiveis = []
        palavra = palavra.lower()
        for letra in palavra:
            if letra not in cEspecial and letra not in lista:
                letrasDisponiveis.append(letra)
        return letrasDisponiveis 

def cores_disponiveis(cores, coresUsadas):
    for i in cores:
        for s in coresUsadas:
            if s == i:
                cores.remove(i)

    return cores

