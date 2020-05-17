import sys
input = sys.stdin.readline
from collections import deque
def main():
    N, M = map( int, input().split())
    E = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map( lambda x:int(x)-1, input().split())
        E[u].append(v)
        E[v].append(u)
    d = deque([0])
    V = [-1]*N
    V[0] = 0
    while d:
        u = d.popleft()
        for v in E[u]:
            if V[v] == -1:
                V[v] = u+1
                d.append(v)
    print("Yes")
    print( "\n".join( map( str, V[1:])))
if __name__ == '__main__':
    main()
