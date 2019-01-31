from copy import deepcopy
N = int( input())
L = [""]
for _ in range(N):
    R = deepcopy(L)
    L = []
    for r in R:
        L.append(r+"a")
        L.append(r+"b")
        L.append(r+"c")
for l in L:
    print(l)
