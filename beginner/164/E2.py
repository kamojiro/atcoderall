import sys
input = sys.stdin.readline

def main():
    import heapq
    N, M, S = map( int, input().split())
    E = [[] for _ in range(N)]
    for _ in range(M):
        u,v,a,b = map( int, input().split())
        u, v = u-1, v-1
        E[u].append((v,a,b))
        E[v].append((u,a,b))
    CD = [ tuple( map( int, input().split())) for _ in range(N)]

    ANS = [[10**12]*2501 for _ in range(N)]
    T = [[False]*2501 for _ in range(N)]
    h = heapq((0,0,S))

    while h:
        d, v, s = heapq.heappop(h)
        if T[v][s]:
            continue
        else:
            T[v][s] = True
        ANS[v][s] = d
        for w, a, b in E[v]:
            
    
    print("\n".join( map( str, ANS[1:])))
        
    
if __name__ == '__main__':
    main()
