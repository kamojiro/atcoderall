N, A = map( int, input().split())
X = list( map( int, input().split()))
dp = [ [0]*(50*N+1) for _ in range(N+1)]
dp[0][0] = 1
for k in range(N):
    x = X[k]
    for i in range(N-1,-1,-1):
        for j in range(50*N+1-x):
            dp[i+1][x+j] += dp[i][j]
ans = 0
for i in range(1,N+1):
    ans += dp[i][i*A]
print(ans)
