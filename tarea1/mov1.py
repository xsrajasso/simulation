from random import random
random()
pos = 0
dur = 10
for t in range(dur):
    if random() < 0.5:
        pos += 1
    else:
        pos -= 1
    print(pos)
