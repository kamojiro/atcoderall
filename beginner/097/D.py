N, M = map( int, input().split())
P = list( map( int, input().split()))
par = [ i for i in range(N)]

def find(x):
    p = par[x]
    if p == x:
        return x
    a = find(p)
    par[x] = a
    return a

for i in range(M):
    x, y = map( int, input().split())
    x, y = x-1, y-1
    bx, by = find(x), find(y)
    par[y] = bx
    par[by] = bx
ans = 0
for i in range(N):
    if find(i) == find(P[i]-1):
        ans += 1
print(ans)
