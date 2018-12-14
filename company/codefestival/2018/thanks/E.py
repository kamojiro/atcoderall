from itertools import accumulate
Q = 10**9+7
T = int( input())
A = list( map( int, input().split()))
dp = [[ [1,1] for _ in range(T*2+1)] for _ in range(T+1)]
for i in range(T):
    L = list( accumulate( [ dp for ]))
    for j in range(T*2):
        dp[i+1][][0] = 

