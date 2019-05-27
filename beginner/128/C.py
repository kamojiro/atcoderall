from itertools import product
N, M = map( int, input().split())
K = [ list( map( int, input().split())) for _ in range(M)]
P = list( map( int, input().split()))
ans = 0
for p in product( range(2), repeat = N):
    t = 1
    for i in range(M):
        cnt = 0
        for j in range(1, K[i][0]+1):
            if p[K[i][j]-1] == 1:
                cnt += 1
        if cnt%2 != P[i]:
            t = 0
            break
    if t == 1:
        ans += 1
print( ans)
