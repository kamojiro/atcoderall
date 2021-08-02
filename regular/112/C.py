#import sys
#input = sys.stdin.readline
from collections import deque
def main():
    N = int( input())
    P = [0] + list(map(lambda x: int(x)-1,input().split()))
    E = [[] for _ in range(N)]
    for v in range(1,N):
        E[P[v]].append(v)
    visited = [False]*N
    visited[0] = True
    d = deque([0])
    H = []
    while d:
        v = d.popleft()
        H.append(v)
        for w in E[v]:
            d.append(w)
    V = [1]*N
    for v in H[::-1]:
        if v == 0:
            continue
        V[P[v]] += V[v]
    # print(V)
    
    ZE = [[] for _ in range(N)]
    G = 10**6
    for v in range(1,N):
        if V[v] %2 == 0:
            ZE[P[v]].append((G+V[v], v))
        else:
            ZE[P[v]].append((V[v], v))
    GE = [deque(sorted(ze)) for ze in ZE]
    ANS = [0,0]
    v = 0
    turn = 0
    ret = [True]*N
    while True:
        # print(v)
        if ret[v]:
            ANS[turn] += 1
            turn ^= 1
            ret[v] = False
            continue
        if GE[v]:
            s, w = GE[v].popleft()
            v = w
            turn ^= 1
        else:
            if v == 0:
                break
            v = P[v]
            turn ^= 1
    print(ANS[0])
    
        
    
    
if __name__ == '__main__':
    main()
