#import sys
#input = sys.stdin.readline
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
    N, M , S = map(int,input().split())
    E = [[] for _ in range(N+1)]
    UV = [tuple(map(int,input().split())) for _ in range(M)]
    for u, v in UV:
        if u > v:
            u, v = v, u
        E[u].append(v)
    V = [i for i in range(N+1)]
    ANS = []
    for v in range(N,0,-1):
        for w in E[v]:
            union(V,v,w)
        if find(V,v) == find(V,S):
            ANS.append(v)
    print("\n".join(map(str,ANS[::-1])))
if __name__ == '__main__':
    main()
