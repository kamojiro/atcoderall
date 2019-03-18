N = int( input())
S = input()
Q = 10**9 + 7
dp = [ [1] + [ 0]*27 for _ in range(N+1)]
dp[0][0] = 1
dp[0][-1] = 1
L = [0]*10000
for i in range(1,N+1):
    a = ord(S[i-1]) - ord("a") + 1
    for j in range(1,27):
        if j == a:
            dp[i][j] = dp[i-1][27]
        else:
            # dp[i][j] = (dp[i-1][j] + (dp[i-1][27] - dp[i-1][a])*dp[i-1][j]//dp[i-1][27])%Q
            dp[i][j] = (dp[i-1][j] + (dp[i-1][j] - L[j*100+a]))%Q
    for j in range(1,27):
        for k in range(j,27):
            L[k*100 + j] += dp[i-1][j] - L[k*100+j]

    dp[i][27] = (dp[i-1][27]*2 - dp[i-1][a] )%Q
    print(dp[i])
print( dp[-1][-1]-1)
