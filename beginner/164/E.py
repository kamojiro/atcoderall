import sys
input = sys.stdin.readline

def dijkstra(N, s, E):
    import heapq
    Ret = [[10**12, 10**12]]*N
    Ret[s] = [0,0]
    C = [False]*N
    q = [(0,0,s)]
    while q:
        d, w, t = heapq.heappop(q)
        if C[t]:
            continue
        C[t] = True
        Ret[t] = [d,w]
        for v, a, b in E[t]:
            if C[v]:
                continue
            if d+b < Ret[v][0]:
                Ret[v] = [d+b, w+a]
                heapq.heappush(q, (d+b,w+a,v))
            elif d+b == Ret[v][0]:
                if w+a < Ret[v][1]:
                    Ret[v][1] = w+a
                    heapq.heappush(q, (d+b,w+a,v))
    return Ret
                


def main():
    import heapq
    P = [pow(2,i) for i in range(51)]
    N, M, S = map( int, input().split())
    E = [[] for _ in range(N)]
    for _ in range(M):
        u,v,a,b = map( int, input().split())
        u, v = u-1, v-1
        E[u].append((v,a,b))
        E[v].append((u,a,b))
    CD = [ tuple( map( int, input().split())) for _ in range(N)]
    # print(dijkstra(N, 1, E))
    q = [(0, -S, 0, 1)]
    ANS = [10**12]*N
    F = [False]*N
    while q:
        t, s, v, l = heapq.heappop(q)
        s = -s
        if F[v]:
            continue
        F[v] = True
        ANS[v] = t
        Dij = dijkstra(N, v, E)
        for j in range(N):
            if l & P[j] == 0 :
                continue
            c, d = CD[j]
            for i in range(N):
                e, m = Dij[i]
                if m <= s:
                    heapq.heappush(q, (t+e, s-m, i, l |P[i]))
                else:
                    n = (m-s+c-1)//c
                    heapq.heappush(q, (t+e+n*d, s+c*n-m, i, l|P[i]))

    print("\n".join( map( str, ANS[1:])))
        
    
if __name__ == '__main__':
    main()
