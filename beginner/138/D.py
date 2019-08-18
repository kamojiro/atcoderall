import sys
input = sys.stdin.readline
from collections import deque
def main():
    N, Q = map( int, input().split())
    E = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map( int, input().split())
        a, b = a-1, b-1
        E[a].append(b)
        E[b].append(a)
    V = [0]*N
    for _ in range(Q):
        p, x = map( int, input().split())
        p -= 1
        V[p] += x
    q = deque([0])
    W = [0]*N
    W[0] = 1
    while q:
        v = q.popleft()
        c = V[v]
        for t in E[v]:
            if W[t] == 1:
                continue
            V[t] += c
            W[t] = 1
            q.append(t)
    print( " ".join( map( str, V)))
if __name__ == '__main__':
    main()
