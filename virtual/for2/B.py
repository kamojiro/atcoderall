import sys
input = sys.stdin.readline
from collections import deque
def main():
    N = int( input())
    E = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map( int, input().split())
        u -= 1
        v -= 1
        E[u].append((v,w))
        E[v].append((u,w))
    V = [-1]*N
    V[0] = 0
    d = deque([(0,0)])
    while d:
        u, l = d.popleft()
        for v,w in E[u]:
            if V[v] == -1:
                V[v] = (l+w)%2
                d.append((v, (l+w)%2))
    print("\n".join( map( str, V)))
    
    
if __name__ == '__main__':
    main()
