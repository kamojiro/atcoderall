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
    dp = [0]*(M+1)
    for j in range(N):
        x, y, z = X[j], Y[j], Z[j]
        for k in range(M-1,-1,-1):
            if dp[k+1] < dp[k] + a*x + b*y + c*z:
                dp[k+1] = dp[k] + a*x + b*y + c*z
    ans = max( ans, dp[M])
    print(dp)
print(ans)
