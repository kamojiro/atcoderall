N = int( input())
A = list( map( int, input().split()))
dp = [0]*N
dp[1] = abs( A[0]-A[1])
for i in range(2,N):
    dp[i] = min( abs(A[i]-A[i-1])+dp[i-1], abs(A[i]-A[i-2]) + dp[i-2])
print(dp[-1])
