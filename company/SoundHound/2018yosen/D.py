import heapq
from collections import defaultdict

def dijkstra(G,D,x,n):
    #Gは隣接頂点
    #Dは各頂点間の距離、逆向きも加えておく(有向なら片方だけ)
    #xはスタート地点
    #nは頂点数
    V = [ 0 for _ in range(n)] #Vはその頂点が確定しているかどうか、確定なら1
    X = [ 10**14 for _ in range(n)] #不確定な経路
    W = [ 0 for _ in range(n)] #Wは最短経路
    H = [(0,x)]
    heapq.heapify(H)
    while H:
        d, p = heapq.heappop(H)
        W[p] = d
        V[p] = 1
        for y in G[p]:
            if V[y] == 0:
                X[y] = min( X[y], d+D[(y,p)])
                heapq.heappush(H, (min(X[y], d + D[(y,p)]),y))
    return W                

n, m, s, t = map( int, input().split())
s, t = s-1, t-1
D_yen = dict()
D_snuke = dict()
G = [ [] for _ in range(n)]
for _ in range(m):
    u, v, a, b = map( int, input().split())
    u, v = u-1, v-1
    G[u].append(v)
    G[v].append(u)
    D_yen[(u,v)] = D_yen[(v,u)] = a
    D_snuke[(u,v)] = D_snuke[(v,u)] = b
C_yen = dijkstra(G,D_yen,s,n)
C_snuke = dijkstra(G,D_snuke,t,n)
ans = 10**14
ANS = [ 0 for _ in range(n)]
for i in range(n):
    ans = min( ans, C_yen[n-1-i] + C_snuke[n-1-i])
    ANS[n-1-i] = ans
for i in range(n):
    print(10**15 - ANS[i])
