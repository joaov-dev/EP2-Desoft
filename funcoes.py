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
    
    if nl not in lista:
        if len(lista) != 0:
            while i<len(lista):
                if lista[i][1] < dist:
                    i+=1
                else:
                    lista.insert(i, nl)
                    break
        else:
            lista.append(nl)

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
    l = []
    cEspecial = ['.', ',', '-', ';', ' ']
    a = palavra. lower()
    for i in range(len(a)):
        l. append (a[i])
    letraAleatoria = random. choice(l)
    todosIguais = True
    for i in a:
        if i not in lista and i not in cEspecial:
            todosIguais = False
    if todosIguais == True:
        return ''
    while letraAleatoria in lista or letraAleatoria in cEspecial:
        letraAleatoria = random. choice(l)
    return letraAleatoria
