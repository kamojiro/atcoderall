from itertools import accumulate
V = [1]*(10**5+1)
P = [0]*(10**5+1)
V[0] = 0
V[1] = 0
for i in range(10**5+1):
    if V[i] == 0:
        continue
    P[i] = 1
    for j in range(2,10**5):
        if i*j >= 10**5:
            break
        V[i*j] = 0
W = [0]*(10**5+1)
for i in range(10**5+1):
    if not V[i]:
        continue
    if V[(i+1)//2] == 1:
        W[i] = 1
accW = list( accumulate(W))
Q = int( input())

for i in range(Q):
    l, r = map( int, input().split())
    print(accW[r] - accW[l-1])
