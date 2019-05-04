N, M, K = map( int,input().split())
A = list( map( int, input().split()))
if N+1 > K*(M+1):
    print(-1)
else:
    dp = [[(0,0)]*(M+1) for i in range(N+1)]
    for i in range(N):
        a = A[i]
        dp[i+1][0] = (dp[i+1][0][0], i+1)
        for m in range(M):
            if dp[i][m][1] == K-1:
                dp[i+1][m+1] = (dp[i][m][0]+a, 0)
            elif dp[i][m+1][0] <= dp[i][m][0] + a:
                dp[i+1][m+1] = (dp[i][m+1][0]+a, 0)
            else:
                if dp[i][m+1][1] >= K:
                    dp[i+1][m+1][1] = (0,0)
                else:
                    dp[i+1][m+1] = (dp[i][m+1][0], dp[i][m+1][1]+1)
    if dp[N][M][0] == 0:
        print(-1)
    else:
        print(dp[N][M][0])
