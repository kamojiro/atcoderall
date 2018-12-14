from itertools import accumulate
S = list( input())
N = int( input())
L = len(S)
V = [0]*(L+1)
S = [ ord(S[i]) for i in range(L)]
for _ in range(N):
    l, r = map( int, input().split())
    V[l-1] += 1
    V[r] += 1
D = list( accumulate(V))
ans = "YES"
for i in range(L-1):
    if 
