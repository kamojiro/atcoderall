import sys
input = sys.stdin.readline
# from collections import defaultdict
def main():
    N, M = map( int, input().split())
    d = dict()
    for _ in range(M):
        a, b, c = map( int, input().split())
        a, b = a-1, b-1
        d[(a,b)] = -c
    INF = 10**14
    V = [INF]*N
    V[0] = 0
    for _ in range(N-1):
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
    if ans == V[N-1]:
        print(-ans)
    else:
        print("inf")
        
if __name__ == '__main__':
    main()
