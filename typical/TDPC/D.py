N, D = map( int, input().split())
a, b, c = [0]*3
hoge = 0
if D == 1:
    hoge = 1
    N = 0
elif D%2 == 0 or D%3 == 0 or D%5 == 0:
    while D%2 == 0:
        D /= 2
        a += 1
    while D%3 == 0:
        D /= 3
        b += 1
    while D%5 == 0:
        D /= 5
        c += 1
    if D > 1:
        hoge = -1
dp = [[[[ 0 for _ in range(c+1)] for _ in range(b+1)] for _ in range(a+1) ] for _ in range(N+1)]
dp[0][0][0][0] = 1
for n in range(N):
    for i in range(a+1):
        for j in range(b+1):
            for k in range(c+1):
                if dp[n][i][j][k] == 0:
                    continue
                else:
                    dp[n+1][i][j][k] += dp[n][i][j][k]/6
                    dp[n+1][min(i+1,a)][j][k] += dp[n][i][j][k]/6
                    dp[n+1][i][min(j+1,b)][k] += dp[n][i][j][k]/6
                    dp[n+1][min(i+2,a)][j][k] += dp[n][i][j][k]/6
                    dp[n+1][i][j][min(k+1,c)] += dp[n][i][j][k]/6
                    dp[n+1][min(i+1,a)][min(j+1,b)][k] += dp[n][i][j][k]/6
if hoge == -1:
    print(0)
elif hoge == 1:
    print(1)
else:
    print(dp[N][a][b][c])
