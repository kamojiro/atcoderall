H, W, N = map( int, input().split())
V = [H-1]*W
X = [ tuple( map( int, input().split())) for _ in range(N)]
X.sort(key = lambda x:x[1])
d = 0
for i in range(N):
    x, y = X[i]
    x, y = x-1, y-1
    if x == y+d:
        d += 1
    elif x > y+d:
        V[y] = min( V[y], x-1)
print( min(V)+1)
