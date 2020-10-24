#import sys
#input = sys.stdin.readline
from heapq import heappop, heappush
def main():
    N, M, S = map(int,input().split())
    E = [[] for _ in range(N+1)]
    UV = [tuple(map(int,input().split())) for _ in range(M)]
    for u, v in UV:
        E[u].append(v)
        E[v].append(u)
    h = [(-S,S)]
    V = [False]*(N+1)
    g = N+1
    while h:
        m, v = heappop(h)
        m = -m
        if V[v]:
            continue
        V[v] = True
        for w in E[v]:
            if not V[w]:
                if w < m:
                    heappush(h,(-w,w))
    print("\n".join(map(str,[ i for i in range(N+1) if V[i]])))
    
if __name__ == '__main__':
    main()
