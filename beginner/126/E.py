def find(A,x):
    p = A[x]
    if p == x:
        return x
    a = find(A,p)
    A[x] = a
    return a
 
def union(A, x, y):
#    bx, by = sorted([find(A,x), find(A,y)]) # bx, by = find(A,x), find(A,y)だと無限ループ。
    if find(A,x) > find(A,y):
        bx, by = find(A,y), find(A,x)
    else:
        bx, by = find(A,x), find(A,y)
    A[y] = bx
    A[by] = bx

N, M = map( int, input().split())
V = [ i for i in range(N)]
for _ in range(M):
    x, y,_ = map( int, input().split())
    union(V, x-1, y-1)
print( sum( [1 for i in range(N) if i == V[i]]))
