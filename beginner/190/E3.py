#import sys
#input = sys.stdin.readline

def bfs(N, E, s, INF=10**10):
    from collections import deque
    V = [INF]*N
    d = deque([s])
    V[s] = 0
    while d:
        v = d.popleft()
        now = V[v]
        for w in E[v]:
            if V[w] < INF:
                continue
            V[w] = now+1
            d.append(w)
    # print(V)
    return V

def tsp(K, G, INF=10**10):
    # K: vertex
    # G[i][j]: the distance from i to j
    # 任意の位置からスタートして全部回りきるまでの距離
    # 元の位置には戻ってこない
    dp = [[INF]*(1 << K) for _ in range(K)]
    for i in range(K):
        dp[i][1 << i] = 0

    for s in range(1 << K):
        for frm in range(K):
            if not s & 1 << frm: # 0 = False
                continue
            if dp[frm][s] == INF:
                continue
            for to in range(K):
                t = s | 1 << to
                if s == t:
                    continue
                dp[to][t] = min(dp[to][t], dp[frm][s] + G[frm][to])
    return min([dp[i][(1 << K) -1] for i in range(K)])


# def find(A,x):
#     p = A[x]
#     if p == x:
#         return x
#     a = find(A,p)
#     A[x] = a
#     return a
 
# def union(A, x, y):
#     if find(A,x) > find(A,y):
#         bx, by = find(A,y), find(A,x)
#     else:
#         bx, by = find(A,x), find(A,y)
#     A[y] = bx
#     A[by] = bx


def main():
    N, M = map(int, input().split())
    AB = [tuple(map(lambda x:int(x)-1,input().split())) for _ in range(M)]
    K = int(input())
    C = list(map(lambda x:int(x)-1,input().split()))
    E = [[] for _ in range(N)]
    INF = 10**10
    for a, b in AB:
        E[a].append(b)
        E[b].append(a)
    G = []
    for c in C:
        O = []
        dist = bfs(N,E,c)
        for g in C:
            O.append(dist[g])
        G.append(O)
    if max([ max(g) for g in G]) == 10**10:
        print(-1)
        return
    pows = [1]
    for _ in range(K-1):
        pows.append(pows[-1]*2)
    P = pow(2,K)

    ans = tsp(K,G)
    if ans == INF:
        print(-1)
    else:
        print(ans+1)
    
    
             
if __name__ == '__main__':
    main()
