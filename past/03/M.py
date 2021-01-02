import sys
input = sys.stdin.readline
from collections import deque
# from heapq import heappop, heappush
def main():
    N, M = map( int, input().split())
    E = [ [] for _ in range(N)]
    for _ in range(M):
        u, v = map( lambda x: int(x)-1, input().split())
        E[u].append(v)
        E[v].append(u)
    s = int( input())-1
    K = int( input())
    T = list( map( lambda x: int(x)-1, input().split()))
    T.sort()
    d = deque([s])
    V = [-1]*N
    V[s] = 0
    while d:
        v = d.popleft()
        t = V[v]
        for u in E[v]:
            if V[u] == -1:
                V[u] = t+1
                d.append(u)
    L = [V[t] for t in T]
    P = []
    for t in T:
        d = deque([t])
        V = [-1]*N
        V[t] = 0
        while d:
            v = d.popleft()
            t = V[v]
            for u in E[v]:
                if V[u] == -1:
                    V[u] = t+1
                    d.append(u)
        P.append([V[t] for t in T])
    # print(L)
    # print(P)
    I = [2**i for i in range(K)]
    g = sum(I)
    INF = 10**11
    V = [[INF]*K for _ in range(2**K)]
    W = [[False]*K for _ in range(2**K)]
    h = []
    S = []
    for i in range(K):
        V[I[i]][i] = L[i]
        # heappush(h,(L[i], I[i], i))
        S.append(I[i])
        # W[I[i]][i] = True
    for _ in range(K-1):
        B = set()
        for s in S:
            for i in range(K):
                for j in range(K):
                    if s & I[j] == 0:
                        B.add(s + I[j])
                        if V[s][i] + P[i][j] < V[s+I[j]][j]:
                            V[s+I[j]][j] = V[s][i] + P[i][j]
        S = list(B)
    print( min(V[g]))
                            
    
    # while h:
    #     # print(h, W)
    #     d, p, v = heappop(h)
    #     if p == g:
    #         print(d)
    #         return
    #     if W[p][v]:
    #         continue
    #     else:
    #         W[p][v] = True
    #     for i in range(K):
    #         # print(p, I[i])
    #         if p & I[i] == 0:
    #             if d + P[v][i] < V[p+I[i]][i]:
    #                 V[p+I[i]][i] = d + P[v][i]
    #                 heappush(h,(d+P[v][i], p+I[i], i))
        
        
    # I = [2**i for i in range(K)]
    # D = [10**11]*(2**K)
    # Z = []
    # for i in range(K):
    #     D[I[i]] = L[i]
    #     Z.append(I[i])
    # for _ in range(K-1):
    #     W = []
    #     for z in Z:
    #         for i in I:
    #             if z & i == 0:
    #                 if D[z] + z < D[z+i]

    
if __name__ == '__main__':
    main()
