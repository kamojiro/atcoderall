Q = 998244353
def getInv(N):#Qはmod
    inv = [0] * (N + 1)
    inv[0] = 1
    inv[1] = 1
    for i in range(2, N + 1):
        inv[i] = (-(Q // i) * inv[Q%i]) % Q
    return inv

N, X = map( int, input().split())
dp = [[0]*(X+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(1, N+1):
    dp[i][0] = 1
    dp[i][1] = 1 + dp[i-1][1]
    for x in range(2,X+1):
        dp[i][x] = (dp[i-1][x] + dp[i-1][x-1] + dp[i-1][x-2])%Q
ans = sum( dp[N][:-1])
F = [1]*(6001)
for i in range(6000):
    F[i+1] = (F[i]*(i+1))%Q
    F[i+1] %= Q
I = getInv(6000)
FI = [1]*(6001)
for i in range(6000):
    FI[i+1] = (FI[i]*I[i+1])%Q
# print(F[:20])
# for i in range(30):
#     print( (F[i]*FI[i])%Q)
if (X+1)%2 == 0:
    dp = [[0]*(X+2) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        dp[i][0] = 1
        for x in range(2,X+2):
            dp[i][x] = (dp[i-1][x] + dp[i-1][x-2])%Q
        dp[i][x] = (dp[i-1][x]*2 + dp[i-1][x-2])%Q
    ans = ( ans + dp[N][X+1])%Q
print(ans%Q)
