#import sys
#input = sys.stdin.readline
def main():
    N, K, M = map(int,input().split())
    dp = [[0]*(N+1) for _ in range(N*K+1)]
    # for i in range(N):
    #     dp[1][i+1] = i+1
    dp[1][1] = 1
    for i in range(2, N*K+1):
        now = 0
        t = i-1
        for j in range(1,N+1):
            dp[i][j] = dp[i-1][j]
            p = (i-1)*j
            k = (i-1)//8+1
            if (p+k)%i == 0:
                dp[i][(p+k)//i] = (dp[i][(p+k)//i] + dp[i-1][j])%M
    # ANS = [0]*N
    # for i in range(N*K):
    #     for j in range(N):
    #         ANS[j] += dp[i+1][j+1]
    print("\n".join(map(str,dp[N*K][1:])))
    # print(dp)
        
if __name__ == '__main__':
    main()
