N = int( input())
dp = [ [0]*12 for _ in range(N+1)]
Q = 10**9 + 7
"0 AGCetc., 1 A, 2 G, 3, AG, 4 GA, 5 AC,6 Ax, 7, AxG, 8 AGA, 9, AGG, 10 AGT, 11, otherwise"
dp[1][11] = 2
dp[1][1] = 1
dp[1][2] = 1
for i in range(2, N+1):
    dp[i][1] = (dp[i-1][3] + dp[i-1][5] +dp[i-1][6] +dp[i-1][8] + dp[i-1][10] + dp[i-1][11])%Q
    dp[i][2] = (dp[i-1][2] + dp[i-1][7] + dp[i-1][9] + dp[i-1][10] + dp[i-1][11])%Q
    dp[i][3] = (dp[i-1][1] + dp[i-1][4] + dp[i][8])%Q
    dp[i][4] = (dp[i-1][2] + dp[i-1][7] + dp[i-1][9])%Q
    dp[i][5] = (dp[i-1][1] + dp[i-1][4])%Q
    dp[i][6] = (dp[i-1][1]*2 + dp[i-1][4]*3 + dp[i-1][8])%Q
    dp[i][7] = (dp[i-1][3] + dp[i-1][6])%Q
    dp[i][8] = dp[i][9] = dp[i][10] = (dp[i-1][3]*3)%Q
    dp[i][0] = (dp[i-1][3] + dp[i-1][4] + dp[i-1][5] + dp[i-1][7] + dp[i-1][8] + dp[i-1][9] + dp[i-1][10])%Q
    dp[i][11] = ( pow(4,i,Q) - sum( dp[i][:12]))%Q
print(dp)
print( sum(dp[N][1:])%Q)
