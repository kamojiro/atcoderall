W = int(input())
N, K = map( int, input().split())
dp = [[0 for _ in range(W+1)] for _ in range(K+1) ]
for k in range(N):
    a, b = map( int, input().split())
    for i in range(K,0,-1):
        for j in range(W,0,-1):
            if a <= j:
                dp[i][j] = max( dp[i][j], dp[i-1][j-a] + b)
print(dp[K][W])
