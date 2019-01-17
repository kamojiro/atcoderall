N, W = map( int, input().split())
WV = [ list( map( int, input().split())) for _ in range(N)]
dp = [0]*(W+1)
for i in range(N):
    w, v = WV[i]
    for i in range(W,-1,-1):
        if i >= w:
            dp[i] = max( dp[i], dp[i-w]+v)
        else:
            break
print( dp[-1])
