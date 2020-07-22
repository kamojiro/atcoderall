#import sys
#input = sys.stdin.readline
from collections import deque
# from numpy import argmax
def bfs(N, E, s):
    V = [-1]*N
    V[s] = 0
    d = deque([s])
    while d:
        v = d.pop()
        t = V[v]+1
        for w in E[v]:
            if V[w] == -1:
                V[w] = t
                d.append(w)
    return V

def main():
    N = int( input())
    AB = [ tuple( map( lambda x: int(x)-1, input().split())) for _ in range(N-1)]
    E = [[] for _ in range(N)]
    for a, b in AB:
        E[a].append(b)
        E[b].append(a)
    V = bfs(N,E,0)
    # romeo = argmax(V)
    romeo = V.index(max(V))
    W = bfs(N,E,romeo)
    # juliet = argmax(W)
    juliet = W.index(max(W))
    print(romeo+1, juliet+1)
    
if __name__ == '__main__':
    main()
