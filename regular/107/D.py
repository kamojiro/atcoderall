#import sys
#input = sys.stdin.readline
Q = 998244353
def main():
    N, K = map(int,input().split())
    dp = [[0]*(N+1) for i in range(N+1)]
    for i in range(K+1):
        dp[0][0] = 1
    for n in range(1,N+1):
        for k in range(N,0,-1):
            dp[n][k] = dp[n-1][k-1]
            if n >= 2*k:
                dp[n][k] += dp[n][2*k]
            dp[n][k] %= Q
    # print(dp)
    print(dp[N][K])
if __name__ == '__main__':
    main()
