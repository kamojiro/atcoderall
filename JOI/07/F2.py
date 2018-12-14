import sys
import heapq
from collections import defaultdict
def dijkstra(V,D,s,g):
    q = [(0,s)]
    X = [10**8 for _ in range(n)]
    W = [-1 for _ in range(n)]
    ans = -1
    while q:
        d, x = heapq.heappop(q)
        W[x] = d
        if x == g:
            ans = W[g]
            break
        if d > X[x]:
            continue
        for y,c in V[x]:
            if W[y] == -1 and d+c < X[y]:
                X[y] = d+c
                heapq.heappush(q,(X[y],y))
    return ans

n, k = map( int, sys.stdin.readline().split())
V = [ set() for _ in range(n)]
D = defaultdict(lambda: 10**6)
for _ in range(k):
    I = list( map( int, sys.stdin.readline().split()))
    if I[0] == 0:
        v, w = I[1:]
        v, w = v-1, w-1
        print(dijkstra(V, D, v, w))
    else:
        v, w, c = I[1:]
        v, w = v-1, w-1
        V[v].add((w,c))
        V[w].add((v,c))
