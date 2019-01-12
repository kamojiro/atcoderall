N = int( input())
H = [ list( map( int, input().split())) for _ in range(N)]
dp = [ [0]*3 for _ in range(N)]
dp[0][0], dp[0][1], dp[0][2] = H[0]
for i in range(1,N):
    a, b, c = H[i]
    dp[i][0] = max( dp[i-1][1]+a, dp[i-1][2]+a)
    dp[i][1] = max( dp[i-1][0]+b, dp[i-1][2]+b)
    dp[i][2] = max( dp[i-1][0]+c, dp[i-1][1]+c)
print( max( dp[-1]))
