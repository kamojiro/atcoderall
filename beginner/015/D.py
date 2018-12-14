W = int(input())
N, K = map( int, input().split())
A = []
B = []
for _ in range(N):
    a, b = map( int, input().split())
    A.append(a)
    B.append(b)
dp = [[[0 for _ in range(N+1)] for _ in range(K+1) ] for _ in range(W+1)]
for i in range(1,W+1):
    for j in range(K+1):
        for k in range(N+1):
            a = A[k-1]
            if a <= i:
                dp[i][j][k] = max( dp[i][j][k-1], dp[i-a][j-1][k-1] + B[k-1])
            else:
                dp[i][j][k] = dp[i][j][k-1]
    print(dp)
print(dp[W][K][N])
    








