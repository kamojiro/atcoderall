import sys
input = sys.stdin.readline
import heapq
from collections import defaultdict
def main():
    N, M, L = map( int, input().split())
    d = defaultdict( int)
    E = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map( int, input().split())
        if c > L:
            continue
        a, b = a-1, b-1
        d[(a,b)] = c
        d[(b,a)] = c
        E[a].append(b)
        E[b].append(a)
    Q = int( input())
    G = [ tuple( map( int, input().split())) for _ in range(Q)]

    V = []
    for i in range(N):
        W = [-1]*N
        h = [(0,-L,i)]
        while h:
            t, g, v = heapq.heappop(h)
            if W[v] == -1:
                W[v] = t
                for w in E[v]:
                    if W[w] == -1:
                        if d[(v,w)] <= -g:
                            heapq.heappush(h, (t, g+d[(v,w)], w))
                        else:
                            heapq.heappush(h, (t+1, -L+d[(v,w)], w))
        V.append(W)
    for s, t in G:
        print( V[s-1][t-1])
    
if __name__ == '__main__':
    main()
