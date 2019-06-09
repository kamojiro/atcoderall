L = input()
l = len(L)
dp = [ [0]*2 for _ in range(l+1)]
dp[0][1] = 1
Q = 10**9+7
for i in range(l):
    if L[i] == "1":
        dp[i+1][1] = dp[i][1]*2%Q
        dp[i+1][0] = (dp[i][0]*3 + dp[i][1])%Q
    else:
        dp[i+1][1] = dp[i][1]
        dp[i+1][0] = dp[i][0]*3%Q
print((dp[l][0]+dp[l][1])%Q)
