from math import ceil
from math import log2
H, W = map( int, input().split())
A = [ input() for _ in range(H)]
T = 0
i = 0
for i in range(H-1):
    if A[i] == A[i+1]:
        T += 1
S = 0
for i in range(W-1):
    check = 1
    for k in range(H):
        if A[k][i] != A[k][i+1]:
            check = 0
            break
    if check == 1:
        S += 1
if H-T == 1:
    print(ceil(log2(W-S)))
elif W-S == 1:
    print(ceil( log2(H-T)))
elif H-T == 2:
    print(2*ceil(log2(W-S)))
elif H-S == 2:
    print(ceil( log2(H-T))*2)
else:
    print( ceil( log2(H-T+1)-1)*ceil(log2(W-S+1)-1))

