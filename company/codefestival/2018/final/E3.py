from heapq import *
N, K = map( int, input().split())
V = [0]*N
ans = 0
q = []
A = list( map( int, input().split()))
for i in range(N):
    heappush(q, (A[i],i))
for _ in range(N):
    a, i = heappop(q)
    for j in range(K):
        if i+j >= N:
            break
        if V[i+j] == 0:
            V[i+j] = 1
            ans += a
print(ans)
