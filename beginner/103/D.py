N, M = map( int, input().split())
Q = [[int(s) for s in input().split()] for _ in range(M)]
Q = sorted(Q)
ans = 1
LQ = len(Q)
stan = Q[0][1]
while LQ != 0:
    k = 1
    if Q[0][0] < stan:
        stan = min(stan,Q.pop(0)[1])
        LQ -= 1
    else:
        ans += 1
        stan = Q[0][1]
print(ans)
