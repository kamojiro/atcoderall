from collections import defaultdict
import heapq as hq
from itertools import permutations
def dijkstra(E, D, start,W):
    q = []
    V = [-1]*N
    V[start] = 0
    # for i in range(start):
    #     V[i] = W[i][start]
    #     for e in E[i]:
    #         if e > start:
    #             hq.heappush(q, (V[i] + D[(i,e)], e))
    for e in E[start]:
        if V[e] == -1:
            hq.heappush(q, (D[start, e],e))
    # print(V, q)
    while q:
        d, v = hq.heappop(q)
        if V[v] >= 0:
            continue
        V[v] = d
        for e in E[v]:
            if V[e] == -1:
                hq.heappush(q, (D[v,e]+d, e))
    return V
N, M, r = map( int, input().split())
R = list( map( int, input().split()))
d = defaultdict( int)
E = [ [] for _ in range(N)]
for _ in range(M):
    a, b, c = map( int, input().split())
    a, b = a-1, b-1
    d[(a,b)] = d[(b,a)] = c
    E[a].append(b)
    E[b].append(a)
W = [ [-1]*N for i in range(N)]
# for i in range(N):
#     W[i] = dijkstra(E,d,i,W)
    # print(W)
for i in range(r):
    W[R[i]-1] = dijkstra(E,d,R[i]-1,W)

ans = 10**9
for P in permutations( range(r)):
    now = R[P[0]]-1
    cans = 0
    for i in range(1,r):
        cans += W[now][R[P[i]]-1]
        now = R[P[i]]-1
    if cans < ans:
        ans = cans
print( ans)
