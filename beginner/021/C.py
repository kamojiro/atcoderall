#import sys
#input = sys.stdin.readline
from collections import deque
Q = 10**9+7
def main():
    N = int( input())
    a, b = map( lambda x: x-1, map( int, input().split()))
    M = int( input())
    E = [[] for _ in range(N)]
    for _ in range(M):
        x, y = map( lambda x: x-1, map( int, input().split()))
        E[x].append(y)
        E[y].append(x)
    V = [-1]*N
    V[a] = 0
    P = [0]*N
    P[a] = 1
    d = deque([a])
    while d:
        v = d.popleft()
        if v == b:
            break
        for w in E[v]:
            if V[w] == -1:
                d.append(w)
                V[w] = V[v]+1
                P[w] += P[v]
            elif V[v]+1 == V[w]:
                P[w] += P[v]
            P[w] %= Q
    print(P[b])
if __name__ == '__main__':
    main()
