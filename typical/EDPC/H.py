H, W = map( int, input().split())
A = [ input() for _ in range(H)]
dp = [[0]*W for _ in range(H)]
dp[0][0] = 1
Q = 10**9+7
for i in range(H):
    for j in range(W):
        if not i == H-1:
            if A[i+1][j] == ".":
                dp[i+1][j] = (dp[i+1][j] + dp[i][j])%Q
        if not j == W-1:
            if A[i][j+1] == ".":
                dp[i][j+1] = (dp[i][j+1] + dp[i][j])%Q
print(dp[H-1][W-1])
            
