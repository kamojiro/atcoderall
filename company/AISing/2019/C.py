from collections import defaultdict
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

H, W = map( int, input().split())
S = [ input() for _ in range(H)]
A = [ i for i in range(H*W)]
D = defaultdict( lambda: (0,0))
for i in range(H):
    for j in range(W):
        if i > 0 and H != 1:
            if S[i][j] != S[i-1][j]:
                union(A, i*W+j, (i-1)*W + j)
        if i < H-1 and H != 1:
            if S[i][j] != S[i+1][j]:
                union(A, i*W+j, (i+1)*W + j)
        if j > 0 and W != 1:
            if S[i][j] != S[i][j-1]:
                union( A, i*W+j, i*W + j-1)
        if j < W-1 and W != 1:
            if S[i][j] != S[i][j+1]:
                union( A, i*W+j, i*W+j+1)
for i in range(H):
    for j in range(W):
        a, b = D[ find(A,i*W+j)]
        if S[i][j] == "#":
            D[ find(A,i*W+j)] = (a+1,b)
        else:
            D[ find(A,i*W+j)] = (a,b+1)
ans = 0
for d in D:
    a, b = D[d]
    ans += a*b
print(ans)
