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
E = [ list( map( int, input().split())) for _ in range(M)]
ans = N*(N-1)//2
V = [1]*N
ANS = [0]*M
ANS[M-1] = ans
A = [ i for i in range(N)]
for i in range(M-1, 0,-1):
    a, b = E[i]
    a, b = find(A,a-1), find(A,b-1)
    if not a == b:
        ans -= V[a]*V[b]
        V[a] = V[b] = V[a]+V[b]
        union(A,a,b)
    ANS[i-1] = ans
    if ans == 0:
        break
for i in range(M):
    print(ANS[i])
