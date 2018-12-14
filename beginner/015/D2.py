W = int(input())
N, K = map( int, input().split())
A = [0]*N
B = [0]*N
dp = [[0 for _ in range(W+1)] for _ in range(K+1) ]
for i in range(N):
    a, b = map( int, input().split())
    A[i] = a
    B[i] = b
for i in range(1,K+1):
    for j in range(W,0,-1):
        for k in range(N):
            a, b = A[k], B[k]
            if a <= j:
                dp[i][j] = max( dp[i][j], dp[i-1][j-a] + b)
        print(dp)
print(dp)
print(dp[K][W])
