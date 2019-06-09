Q = 10**9+7
N, M = map( int, input().split())
V = [0]*(N+1)
dp = [0]*(N+1)
dp[0] = 1
for _ in range(M):
    a = int( input())
    V[ a] = 1
for i in range(N):
    dp[i] %= Q
    if i == N-1:
        dp[N] += dp[N-1]
        continue
    if V[i+1] == 0:
        dp[i+1] += dp[i]
    if V[i+2] == 0:
        dp[i+2] += dp[i]
ans = dp[N]%Q
print(ans)
