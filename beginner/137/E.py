import sys
input = sys.stdin.readline

def main():
    N, M, P = map( int, input().split())
    d = dict()
    for _ in range(M):
        a, b, c = map( int, input().split())
        a, b = a-1, b-1
        d[(a,b)] = P-c

    INF = float("inf")
    V = [INF]*N
    V[0] = 0
    for _ in range(N):
        for e in d:
            s, t = e
            if V[s] + d[e] < V[t]:
                V[t] = V[s] + d[e]
    ans = V[N-1]
    for _ in range(N):
        for e in d:
            s, t = e
            if V[s] + d[e] < V[t]:
                V[t] = V[s] + d[e]

    if V[N-1] < ans:
        print(-1)
        return
    print( max(-ans,0))
    
if __name__ == '__main__':
    main()
