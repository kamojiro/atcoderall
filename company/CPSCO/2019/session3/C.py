from itertools import accumulate
N = int( input())
T = [0]*(10**6+1)
for _ in range(N):
    s, t= map( int, input().split())
    T[s-1] += 1
    T[t-1] -= 1
C = [0] + list( accumulate(T))
ans = 0
for i in range(10**6+1):
    if C[i] == 0 and C[i+1] > 0:
        ans += 1
print( ans)
