import sys
input = sys.stdin.readline
from collections import deque
from copy import deepcopy
def main():
    N, M, P = map( int, input().split())
    E = []
    rE = [[] for _ in range(N)]
    
    for _ in range(M):
        a, b, c = map( int, input().split())
        a, b = a-1, b-1
        E.append((a,b,c-P))
        rE[b].append(a)
    # 頂点Nに到達する頂点
    G = [False]*N
    G[N-1] = True
    q = deque([N-1])
    while q:
        v = q.popleft()
        for w in rE[v]:
            if G[w] == False:
                G[w] = True
                q.append(w)
    # Bellman-Ford
    V = [None]*N
    V[0] = 0
    I = sum([1 for i in range(N) if G[i] == True])
    for _ in range(I-1):
        for s, t, cost in E:
            if V[s] == None or G[t] == False:
                continue
            if V[t] == None:
                V[t] = V[s] + cost
                continue
            if V[s] + cost > V[t]:
                V[t] = V[s] + cost
    W = deepcopy(V) #[ V[i] for i in range(N)]
    for _ in range(I-1):
        for s, t, cost in E:
            if V[s] == None or G[t] == False:
                continue
            if V[t] == None:
                V[t] = V[s] + cost
                continue
            if V[s] + cost > V[t]:
                V[t] = V[s] + cost
    for i in range(N):
        if W[i] == None or G[i] == False:
            continue
        if V[i] > W[i]: # 頂点iは、頂点Nに到達するので、負（正？）閉路は伝播する
            print(-1)
            return

    print( max(W[-1], 0))
if __name__ == '__main__':
    main()
