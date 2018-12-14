from heapq import *
def find(A,x) -> int:
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

N = int( input())
X = [(0,0)]*N
Y = [(0,0)]*N
E = [(0,0)]*N
for i in range(N):
    x, y = map( int, input().split())
    X[i] = (x,i)
    Y[i] = (y,i)
    E[i] = (x,y)
X.sort()
Y.sort()
H = []
heapify(H)
for i in range(N-1):
    x1, j1 = X[i]
    x2, j2 = X[i+1]
    y1, k1 = Y[i]
    y2, k2 = Y[i+1]
    heappush(H,(x2-x1, j1, j2))
    heappush(H, (y2-y1, k1, k2))
ans = 0
V = [ i for i in range(N)]
while H:
    w,s,t = heappop(H)
    if find(V,s) != find(V,t):
        union(V,s,t)
        ans += w
print(ans)
