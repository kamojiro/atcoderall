D, N = map( int, input().split())
T = [ int(input()) for _ in range(D)]
mM = []
C = []
for _ in range(N):
    a, b, c = map( int, input().split())
    mM.append([a,b])
    C.append(c)
t = T[0]
Cminnow = 100
Cmaxnow = 0
dp = [ [ -1 for _ in range(N)] for _ in range(D)]
for i in range(N):
    if mM[i][0] <= t and t <= mM[i][1]:
        dp[0][i] = 0
for i in range(1,D):
    t = T[i]
    Cmin = 100
    CMax = 0
    for j in range(N):
        if mM[j][0] <= t and t <= mM[j][1]:
            for k in range(N):
                if not dp[i-1][k] == -1:
                    dp[i][j] = max(dp[i][j], dp[i-1][k] + abs(C[k]-C[j]))
print(max(dp[D-1]))
