#import sys
#input = sys.stdin.readline
import numpy as np
Q = 10**9+7
def main():
    N, M = map( int, input().split())
    S = np.array( input().split(), dtype=np.int32)
    T = np.array( input().split(), dtype=np.int32)
    dp = np.zeros((N+1,M+1), dtype=np.int64)
    dp[0][0] = 1
    sums = np.zeros((N+1,M+1))
    for i in range(1,N+1):
        same = (T == S[i-1])
        print(same)
        dp[i,] += dp[i-1,]
        print(dp[i])
        dp[i,1:][same] = dp[i-1,:N][same]
        dp[i,1:] -= dp[i-1,:N]
        dp[i].cumsum()
        dp[i] %= Q
    print(dp)
    print( dp[N,M])
if __name__ == '__main__':
    main()
