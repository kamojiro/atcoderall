from collections import defaultdict
Q = 998244353
D = defaultdict( int)
N, M = map( int, input().split())
L = (N**2-N)//2
Ld = N
ans = 1
diag = [-1]*(N+1)
A = [(0,0,0)]*M
for _ in range(M):
    a, b, c = map( int, input().split())
    if a == b:
        D[(a,b)] = c+2
        Ld -= 1
    else:
        L -= 1
        D[(a,b)] = c+2
for i in range(N-1):
    if D[(i,i)] >= 2 and D[(i,i+1)] >= 2 and D[(i+1,i)] >= 2 and D[(i+1,i+1)] >= 2:
        if not (D[(i,i)] + D[(i,i+1)] + D[(i+1,i)] + D[(i+1,i+1)])%2 == 0:
            ans = 0
print( ans*pow(2,L+Ld,Q))
