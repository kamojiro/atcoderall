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

from collections import Counter
N = int( input())
V = [ i for i in range(N)]
for i in range(N):
    a = int( input()) - 1
    union(V,i,a)
W = [0]*N
# for i in range(N):
#     W[i] = find(V,i)
# C = Counter(W)
# コメントアウト部分がなくても通った。偶然？
C = Counter(V)
ans = 0
for x in C:
    if C[x]%2 == 1:
        ans = -1
        break
    else:
        ans += C[x]//2
print(ans)
