N = int( input())
C = [ int( input()) for _ in range(N)]
dp = [1]*(N+1)
colors = [1]*(2*10**5+1)
S = [-1]*(2*10**5+1)
Q = 10**9+7
for i in range(N):
    if i >= 1:
        if C[i] == C[i-1]:
            dp[i+1] = dp[i]
            continue
    if S[C[i]] == -1:
        dp[i+1] = dp[i]
        S[C[i]] = 1
        if i >= 1:
            S[C[i]] = dp[i]
        continue
    dp[i+1] = (dp[i] + S[C[i]])%Q
    S[C[i]] += dp[i]
    S[C[i]] %= Q
print(dp[N])
