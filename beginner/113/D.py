H, W, K = map( int, input().split())
C = [1, 1, 2, 3, 5, 8, 13, 21] #0に横棒が隣接している
Q = 10**9 + 7
dp = [[1]+[0]*(W-1) for _ in range(H+1)]
if W == 1:
    H = 0
for i in range(1,H+1):
    for j in range(W):
        if j == 0:
            dp[i][0] = (dp[i-1][0]*C[W-1] + dp[i-1][1]*C[W-2])%Q
        elif j == W-1:
            dp[i][W-1] = (dp[i-1][W-1]*C[W-1] + dp[i-1][W-2]*C[W-2])%Q
        else:
            dp[i][j] = (dp[i-1][j]*C[j]*C[W-j-1] + dp[i-1][j-1]*C[j-1]*C[W-j-1] + dp[i-1][j+1]*C[j]*C[W-j-2])%Q
print(dp[H][K-1])
