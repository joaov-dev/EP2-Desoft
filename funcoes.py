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
