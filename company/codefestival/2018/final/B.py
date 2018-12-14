from math import log10
N, M = map( int, input().split())
R = list( map( int, input().split()))
Log = [0]*(N+1)
for i in range(1, N+1):
    Log[i] = Log[i-1] + log10(i)
ans = 0
h = N
for i in range(M):
    r = R[i]
    ans += Log[h] - Log[h-r]-Log[r]
    h -= r
ans -= log10(M)*N
ans = -ans
print( int( ans+1))
