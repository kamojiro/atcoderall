#import sys
#input = sys.stdin.readline
from collections import deque

def find(A,x):
    p = A[x]
    if p == x:
        return x
    a = find(A,p)
    A[x] = a
    return a
 
def union(A, x, y):
    if find(A,x) > find(A,y):
        bx, by = find(A,y), find(A,x)
    else:
        bx, by = find(A,x), find(A,y)
    A[y] = bx
    A[by] = bx

def main():
    N, M = map(int,input().split())
    UVC = [ tuple(map( lambda x:int(x)-1, input().split())) for _ in range(M)]
    V = [ i for i in range(N)]
    E = [[] for _ in range(N)]
    T = [0]*N
    for u,v,c in UVC:
        if find(V,u) == find(V,v):
            continue
        union(V,u,v)
        E[u].append((v,c))
        E[v].append((u,c))
        T[u] += 1
        T[v] += 1
    ANS = [-1]*N
    d = deque([0])
    ANS[0] = E[0][0][1]
    while d:
        u = d.popleft()
        nc = ANS[u]
        for v, c in E[u]:
            if ANS[v] >= 0:
                continue
            if c == nc:
                ANS[v] = (c+1)%N
            else:
                ANS[v] = c
            d.append(v)
    print("\n".join(map(lambda x: str(x+1), ANS)))
    
if __name__ == '__main__':
    main()
