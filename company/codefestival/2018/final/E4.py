from collections import deque, defaultdict
from heapq import *
N, K = map( int, input().split())
A = list( map( int, input().split()))
ND = defaultdict( int)
D = defaultdict( int)
h = []
ans = 0
for i in range(N):
    a = A[i]
    if D[a] == ND[a]:
        heappush(h, a)
    D[a] += K
    b = heappop(h)
    ans += b
    ND[b] += 1
    if not ND[b] == D[b]:
        heappush(h, b)
print(ans)
