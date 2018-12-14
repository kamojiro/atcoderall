N, M, Q = map( int, input().split())
LS = [ 0 for _ in range(N+1)]
Mid = [ 0 for _ in range(N+1)]
One = [ 0 for _ in range(N+1)]
for _ in range(M):
    L, R = map( int, input().split())
    if L == R-1:
        One[L] += 1
    for i in range(1,L+1):
        LS[i] += 1
    if L != N and R!= N:
        for i in range(L+1, R+1):
            Mid[i] += 1
    
for _ in range(Q):
    p, q = map(int, input().split())
    if p == q:
        print(LS[p] - LS[(p+1)%N] - Mid[p] - One[p])
    else:
        print(LS[p] - LS[q] - Mid[q] - One[q])








