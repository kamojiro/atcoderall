from itertools import product
N, A, B, C = map( int, input().split())
L = [ int( input()) for _ in range(N)]
T = [-A, -B, -C]
ans = 10**4
for V in product( range(4), repeat = N):
    ANS = [-A,-B,-C]
    mp = 0
    for i in range(N):
        if V[i] == 3:
            continue
        if ANS[V[i]] > T[V[i]]:
            mp += 10
        ANS[V[i]] += L[i]
    if ANS[0] == -A or ANS[1] == -B or ANS[2] == -C:
            continue
    ans = min( ans, sum( list( map( abs, ANS))) + mp)
print(ans)
