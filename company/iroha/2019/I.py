from collections import defaultdict
import heapq
N, M, K = map( int, input().split())

A = [0]*M
B = [0]*M
C = [0]*M
D = defaultdict( int)
E = [ [] for _ in range(N)]
V = [-1]*N
h = [(0,0,-1)]
for i in range(M):
    a, b, c = map( int, input().split())
    a, b = a-1, b-1
    E[a].append(b)
    E[b].append(a)
    D[(a,b)] = D[(b,a)] = c
while h:
    d, v, t = heapq.heappop(h)
    if V[v] != -1:
        continue
    V[v] = d
    
    while
    

