import sys
input = sys.stdin.readline
from collections import deque
def main():
    N, M = map( int, input().split())
    d = dict()
    E = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map( int, input().split())
        a, b = a-1, b-1
        E[a].append(b)
        d[(a,b)] = c
    #loopcheck
    V = [0]
    for s in range(N):
        if V[s] == 1:
            continue
        q = deque([s])
        while d:
            v = q.popleft()
            for w in E[v]:
                if V[w] == 1:
                    print("inf")
                    return
                V[w] = 1
                d.append(w)
    
        
if __name__ == '__main__':
    main()
