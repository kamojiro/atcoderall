from copy import deepcopy
N, K = map( int, input().split())
A = list( map( int, input().split()))
RA = A.sort( reverse = True)
L = 0
R = N-1
while R-L != 1:
    now = (L+R)//2
    B = [0]
    V = [0]*(K+1)
    for j in range(N):
        if j == now:
            continue
        a = A[j]
        C = []
        for b in B:
            if b + a <= K:
                if V[b+a] == 0:
                    V[b+a] = b+a
                    C.append(b+a)
        B = deepcopy(C)
    v = max(V)
    if v < K and K <= v+A[now]:
        R = now
    else:
        L = now

print(R)
