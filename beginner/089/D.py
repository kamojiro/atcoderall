H, W, D = map( int, input().split())
A = [ list( map( int, input().split())) for _ in range(H)]
P = [(0,0)]*(H*W+1)
for i in range(H):
    for j in range(W):
        P[A[i][j]] = (i,j)
d = [0]*(H*W+1)
for i in range(D+1,H*W+1):
    d[i] = d[i-D] + abs(P[i][0] - P[i-D][0]) + abs(P[i][1] - P[i-D][1])
Q = int( input())
for _ in range(Q):
    L, R = map( int, input().split())
    print(d[R]-d[L])
