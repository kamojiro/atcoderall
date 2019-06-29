import sys
input = sys.stdin.readline
from collections import deque
def main():
    N, M = map( int, input().split())
    E = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map( int, input().split())
        u, v = u-1, v-1
        E[u].append(v)
    s, t = map( int, input().split())
    s, t = s-1, t-1
    d = deque([s])
    V = [10**9]*(N*3)
    V[s] = 0
    while d:
        u = d.popleft()
        r, v = u//N,u%N
        c = V[u]
        if r == 0 and v == t:
            print(c//3)
            return
        r = (r+1)%3
        for z in E[v]:
            if c+1 < V[r*N+z]:
                V[r*N+z] = c+1
                d.append(r*N+z)
    print(-1)
if __name__ == '__main__':
    main()

