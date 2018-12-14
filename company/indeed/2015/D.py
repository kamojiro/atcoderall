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

H, W = map( int, input().split())
sx, sy = map( int, input().split())
gx, gy = map( int, input().split())
P = [ list( map( int, input().split())) for _ in range(H)]
V = [ i for i in range(H*W)]
sx, sy = sx-1, sy-1
gx, gy = gx-1, gy-1
ans = P[sy][sx]
K = []
heapify(K)
if sx !=  max(sx-1,0):
    heappush(K, ( -P[sy][sx-1]*P[sy][sx] , sx-1, sy))
if sx != min(sx+1,W-1):
    heappush(K, ( -P[sy][sx+1]*P[sy][sx] , sx+1, sy))
if sy != max(sy-1, 0):
    heappush(K,  ( -P[sy-1][sx]*P[sy][sx], sx, sy-1))
if sy != min(sy+1,H-1):
    heappush(K,  ( -P[sy+1][sx]*P[sy][sx], sx, sy+1))
s = sx*H+sy
while K:
    p, x, y = heappop(K)
    if find(V, sx*H + sy) != find(V, x*H+y):
        union(V, sx*H + sy,  x*H+y)
        ans += P[y][x]
        ans += -p
        if x !=  max(x-1,0):
            if find(V, (x-1)*H+y) != find(V, s):
                heappush(K, ( -P[y][x-1]*P[y][x] , x-1, y))
        if x != min(x+1,W-1):
            if find(V, (x+1)*H + y) != find(V,s):
                heappush(K, ( -P[y][x+1]*P[y][x] , x+1, y))
        if y != max(y-1, 0):
            if find(V, x*H+y-1) != find( V, s):
                heappush(K,  ( -P[y-1][x]*P[y][x], x, y-1))
        if y != min(y+1,H-1):
            if find(V, x*H+y+1) != find(V,s):
                heappush(K,  ( -P[y+1][x]*P[y][x], x, y+1))
print(ans)
