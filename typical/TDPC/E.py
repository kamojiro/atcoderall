D = int(input())
N = list(input())
N = N[::-1]
L = len(N)
N = [ int(x) for x in range(N)]
Q = 10**9 + 7
dp = [[ 0 for _ in range(D)] for _ in range(L+1)]
for i in range(1,L+1):
    n = 
    for j in range(N[i]+1):
        
    for j in range(D):
        for k in range(D):
            dp[i][(j+k)%D] = (dp[i][(j+k)%D] + dp[i-1][j])%Q
ans = 0
cnt = 0
for x in N:
    cnt += x
    for i in range(1,x+1):
        for k in range(10):
            if (i+k)%D == 0:
                ans +=
        

