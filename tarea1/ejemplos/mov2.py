from random import random
from math import fabs
from distance import ed_orig, md_orig
from caminata import caminata

pos = 0
mayor = 0
dur = 100
for t in range(dur):
    if random() < 0.5:
        pos += 1
    else:
        pos -= 1
    dist = int(fabs(pos))
    if dist > mayor:
        mayor = dist
print(mayor)
