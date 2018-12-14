def check(a,b,c,d,V):
    V[a][b] += 1
    V[c][d] += 1
    V[a][d] -= 1
    V[c][b] -= 1


N, K = map( int, input().split())
L = K*2
KK = [[0]*(L+1) for _ in range(L+1)]

for i in range(N):
    x, y, c = input().split()
    x, y = int(x), int(y)
    if c == "B":
        x, y = x%L, y%L
    else:
        x, y = (x+K)%L, (y+K)%L
    x_, y_ = x%K, y%K
