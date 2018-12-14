from heapq import *
from collections import Counter
H, W = map( int, input().split())
C = [ list( map( int, input().split())) for _ in range(10)]
A = [ list( map( int, input().split())) for _ in range(H)]
N = [0]*10
for i in range(H):
    CA = Counter(A[i])
    for j in range(10):
        N[j] += CA[j]
L = [(0,1)]
V = [-1]*10
while L:
    d, v = heappop(L)
    if not V[v] == -1:
        continue
    V[v] = d
    for i in range(10):
        if V[i] == -1:
            heappush(L, (d+C[i][v], i))
ans = 0
for i in range(10):
    ans += V[i]*N[i]
print(ans)
