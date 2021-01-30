#import sys
#input = sys.stdin.readline
from collections import deque
def main():
    N = int( input())
    AB = [ tuple(map( lambda x: int(x)-1, input().split())) for _ in range(N-1)]
    Q = int( input())
    TEX = [ tuple(map( int, input().split())) for _ in range(Q)]
    E = [[] for _ in range(N)]
    for a, b in AB:
        E[a].append(b)
        E[b].append(a)
    before = [-1]*N
    visited = [False]*N
    turn = []
    d = [0]
    while d:
        v = d.pop()
        if visited[v]:
            continue
        turn.append(v)
        visited[v] = True
        for w in E[v]:
            if not visited[w]:
                d.append(w)
                before[w] = v
    V = [0]*N
    for t,e,x in TEX:
        a, b = AB[e-1]
        if t == 1:
            if before[b] == a:
                V[0] += x
                V[b] -= x
            else:
                V[a] += x
        else:
            if before[b] == a:
                V[b] += x
            else:
                V[0] += x
                V[a] -= x
    #     print(t,e,x,V)
    # print(V)
    for v in turn:
        for w in E[v]:
            if before[v] == w:
                continue
            V[w] += V[v]
    print("\n".join(map(str,V)))
                

        
        
if __name__ == '__main__':
    main()
