from copy import deepcopy
N, K = map( int, input().split())
A = list( map( int, input().split()))
ans = N
for i in range(N):
    B = [0]
    V = [0]*(K+1)
    for j in range(N):
        if j == i:
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
    if v < K and K <= v+A[i]:
        ans -= 1
print(ans)
                    
        
