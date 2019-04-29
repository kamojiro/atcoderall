N = int( input())
P = list( map( float, input().split()))
t = N//2+1
dp = [0]*(t+1)
dp[0] = 1
for p in P:
    for i in range(t-1,-1,-1):
        dp[i], dp[i+1] = dp[i]*(1-p), dp[i+1] + dp[i]*p
print(dp[t])
