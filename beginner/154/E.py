#import sys
#input = sys.stdin.readline
def main():
    A = input()
    K = int( input())
    N = len(A)
    dp = [ [ [0]*(K+1) for _ in range(2)] for _ in range(N)]
    t = int( A[0])
    dp[0][0][1] = 1
    dp[0][1][1] = t-1
    for i in range(N):
        dp[i][1][0] = 1
    for i in range(1,N):
        t = int(A[i])
        if t == 0:
            for k in range(1,K+1):
                dp[i][0][k] = dp[i-1][0][k]
        else:
            for k in range(K):
                dp[i][0][k+1] = dp[i-1][0][k]
        if t == 0:
            for k in range(1,K+1):
                dp[i][1][k] = dp[i-1][1][k] + dp[i-1][1][k-1]*9
        else:
            for k in range(1,K+1):
                dp[i][1][k] = dp[i-1][1][k] + dp[i-1][1][k-1]*9 + dp[i-1][0][k-1]*(t-1) + dp[i-1][0][k]
    print(dp[N-1][0][K] + dp[N-1][1][K])
if __name__ == '__main__':
    main()
