from random import getrandbits, randint
import matplotlib.pyplot as plt
from math import sqrt, fabs

def experimento(dim, dur, eucl):
    pos = [0] * dim
    mayor = 0
    delta = getrandbits(dur)
    for t in range(dur):
        pos[randint(0, dim - 1)] += 1 if delta % 2 == 0 else -1
        delta >>= 1
    mayor = max(mayor, sqrt(sum([p**2 for p in pos])) if eucl else sum([fabs(p) for p in pos]))
    return mayor
if __name__ == "__main__":
    dimension = [d for d in range(1, 9)] # de uno a ocho
    duracion = 200
    replicas = 100
    results = None
    p = [(d, duracion, True) for d in dimension]
    p += [(d, duracion, False) for d in dimension]
    param = p * replicas
    results =(experimento, param)
print(results)
