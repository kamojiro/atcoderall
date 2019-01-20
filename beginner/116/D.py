N, K = map( int, input().split())
T = [(0,0)]*N
for i in range(N):
    t, d = map( int, input().split())
    T[i] = (d,t)
T.sort( key= None, reverse = True)
C = T[:K]
AC = T[K:]
kiso = 0
s = 0
S = [0]*(N+1)
for i in range(K):
    d, t = T[i]
    kiso += d
    if S[t] == 0:
        S[t] = 1
        s += 1
    else:
        S[t] += 1
ans = kiso + s**2
C.sort()
r = 0

for i in range(K):
    d, t = C[i]
    if S[t] >= 2:
        while r < N-K:
            if S[ AC[r][1]] == 0:
                S[t] -= 1
                S[ AC[r][1]] += 1
                s += 1
                kiso -= d
                kiso += AC[r][0]
                r += 1
                break
            r += 1
    ans = max( ans, kiso + s**2)
print( ans)
