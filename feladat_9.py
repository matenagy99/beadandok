import sys
import numpy as np
import random


def szoroz(amtx, bmtx):
    szorzat = np.zeros((s1, o2))
    if o1 != s2:
        return "A két mátrix nem szorozható össze!"
    for i in range(0, s1):
        for j in range(0, o2):
            for k in range(0, s2):
                szorzat[i][j] += amtx[i][k] * bmtx[k][j]
    return szorzat


s1 = int(sys.argv[1])
o1 = int(sys.argv[2])
s2 = int(sys.argv[3])
o2 = int(sys.argv[4])

A = np.random.randint(0, 10, (s1, o1))
B = np.random.randint(0, 10, (s2, o2))

print(szoroz(A, B))
