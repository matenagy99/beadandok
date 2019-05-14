import numpy as np
import random
def leghosszabbnovekvo(lista):
    n = len(lista)
    novekvok = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if lista[i] > lista[j] and novekvok[i] < novekvok[j] + 1:
                novekvok[i] = novekvok[j] + 1

    maximum = 0
    for i in range(n):
        maximum = max(maximum, novekvok[i])

    return maximum

ls=np.random.randint(1,10,5)
ls1=np.random.randint(1,10,5)

print(ls)
print(ls1)

print(leghosszabbnovekvo(ls))
print(leghosszabbnovekvo(ls1))