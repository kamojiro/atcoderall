P = [(1,1,1), (1,1,-1), (1,-1,1), (1,-1,-1), (-1,1,1), (-1,1,-1), (-1,-1,1), (-1,-1,-1)]
N, M = map( int, input().split())
X = [0]*N
Y = [0]*N
Z = [0]*N
ans = 0
for i in range(N):
    X[i], Y[i], Z[i] = map( int, input().split())
for i in range(8):
    a, b, c = P[i]
    W = [0]*N
    for j in range(N):
        W[j] = a*X[j] + b*Y[j] + c*Z[j]
    W.sort(key=None, reverse = True)
    ans = max( ans, sum(W[:M]))
print(ans)
