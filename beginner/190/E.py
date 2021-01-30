#import sys
#input = sys.stdin.readline
from collections import deque
from heapq import heappush, heappop
def dfs(N, E, s):
    V = [-1]*N
    d = deque([s])
    V[s] = 0
    while d:
        v = d.popleft()
        now = V[v]
        for w in E[v]:
            if V[w] > -1:
                continue
            V[w] = now+1
            d.append(w)
    return V

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
    for a, b in AB:
        E[a].append(b)
        E[b].append(a)
    G = []
    for c in C:
        O = []
        dist = dfs(N,E,c)
        for g in C:
            O.append(dist[g])
        G.append(O)
    pows = [1]
    for _ in range(K-1):
        pows.append(pows[-1]*2)
    P = pow(2,K)

    F = [[] for _ in range(K)]
    Z = [i for i in range(K)]
    for i in range(K):
        for j in range(K):
            if i == j:
                continue
            if G[i][j] == -1:
                continue
            # union(Z,i,j)
            F[i].append((j, pows[j]))
    # for z in Z:
    #     if z > 0:
    #         print(-1)
    #         return
    INF = 10**10
    V = [[INF]*P for _ in range(K)]
    h = []
    for i, p in enumerate(pows):
        V[i][p] = 0
        heappush(h,(0, i*P+p))
    count = 0
    while h:
        d, ip = heappop(h)
        i, p = ip//P, ip%P
        count += 1
        if count > 10:
            break
        if p == P-1:
            break
        for j, q in F[i]:
            if p & q == 0:
                if d+G[i][j]<V[i][p|q]:
                    V[j][p|q] = d+G[i][j]
                    heappush(h, (V[j][p|q], j*P+(p|q)))
    ans = INF
    for i in range(K):
        if V[i][P-1] < ans:
            ans = V[i][P-1]
    if ans == INF:
        print(-1)
    else:
        print(ans+1)
        
    
    
             
if __name__ == '__main__':
    main()
