import sys
input = sys.stdin.readline
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
    N, Q = map( int, input().split())
    TUV = [ tuple( map( int, input().split())) for _ in range(Q)]
    G = [ i for i in range(N)]
    ANS = []
    for t, u, v in TUV:
        if t == 0:
            union(G,u,v)
        else:
            if find(G,u) == find(G,v):
                ANS.append(1)
            else:
                ANS.append(0)
    print("\n".join( map( str, ANS)))
        
if __name__ == '__main__':
    main()
