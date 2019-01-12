N, K = map( int, input().split())
H = list( map( int, input().split()))
dp = [0]*N
for i in range(1,N):
    h = H[i]
    now = dp[i-1] + abs( h - H[i-1])
    for j in range( max(i-K,0), i):
        if now > dp[j] + abs( h - H[j]):
            now = dp[j] + abs( h - H[j])
    dp[i] = now
print( dp[-1])
