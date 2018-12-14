N, M = map( int, input().split())
Q = [[int(s) for s in input().split()] for _ in range(M)]
Q = sorted(Q)
ans = 1
stan = Q[0][1]
for i in range(M):
    if Q[i][0] < stan:
        stan = min(stan,Q[i][1])
    else:
        ans += 1
        if i == M-1:
            break
        else:
            stan = Q[i][1]
print(ans)
