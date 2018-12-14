N, Q = map( int, input().split())
V = [ i for i in range(N)]
def find(x):
    p = V[x]
    if p == x:
        return x
    a = find(p)
    V[x] = a
    return a

for _ in range(Q):
    P, A, B = map( int, input().split())
    if P == 0:
        A, B = A-1, B-1
        pA, pB = find(A), find(B)
        V[B] = pA
        V[pB] = pA
    else:
        if find(A-1) == find(B-1):
            print('Yes')
        else:
            print('No')
    
