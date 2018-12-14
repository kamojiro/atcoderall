import heapq
def dijkstra(V):
    W = [ 10**14 for _ in range(N)]
    W[0] = 0
    q = [(0,0)]
    while q:
        d, x = heapq.heappop(q)
        if W[x] < d:
            continue
        for y, l in V[x]:
            if W[y] > d+l:
                W[y] = d+l
                heapq.heappush(q, (W[y], y))
    return W

N, M, T = map( int, input().split())
A = list( map(int, input().split()))
V = [ [] for _ in range(N)]
X = [ [] for _ in range(N)]
for _ in range(M):
    a, b, c = map( int, input().split())
    a, b = a-1, b-1
    V[a].append((b,c))
    X[b].append((a,c))

ans = A[0]*T
DV = dijkstra(V)
DX = dijkstra(X)
for i in range(N):
    if DV[i] + DX[i] < T:
        ans = max( ans, A[i]*(T - DV[i] - DX[i]))
print(ans)
