N, K = map( int, input().split())
A = list( map( int, input().split()))
# 1の個数をそれぞれの桁でカウントしたい
V = [0]*41
for a in A:
    for i in range(40,-1,-1):
        if a%2 == 0:
            pass
        else:
            V[i] += 1
        a //= 2
        if a == 0:
            break
W = [0]*41
for i in range(40,-1,-1):
    if K%2 == 0:
        pass
    else:
        W[i] += 1
    K //= 2
    if K == 0:
        break
ans = 0
check = 0
dp = [[-1]*2 for _ in range(42)]
dp[0][0] = 0
for i in range(41):
    if dp[i][1] != -1:
        dp[i+1][1] = dp[i][1] + (2**(40-i))*max(V[i], N-V[i])
    if dp[i][0] != -1:
        if W[i] == 1:
            dp[i+1][1] = max( dp[i+1][1], dp[i][0]+(2**(40-i))*V[i] )
    if dp[i][0] != -1:
        if W[i] == 1:
            dp[i+1][0] = dp[i][0] + (2**(40-i))*(N-V[i])
        else:
            dp[i+1][0] = dp[i][0] + (2**(40-i))*V[i]
print( max( dp[-1][0], dp[-1][1]))
