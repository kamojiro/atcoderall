N, W = map( int, input().split())
dp = [10**9+1]*(10**5+2)
dp[0] = 0
for _ in range(N):
    w, v = map( int, input().split())
    #iを実現しうる最小のwを更新すればよいのでは
    for i in range(10**5,0,-1):
        if i <= v:
            dp[i] = min( dp[i], w)
        else:
            if dp[i-v] + w <= W:
                dp[i] = min( dp[i-v] + w, dp[i])
print( dp.index(10**9+1)-1)
