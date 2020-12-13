#import sys
#input = sys.stdin.readline
def main():
    N, M = map( int, input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    dp = [[0]*(M+1) for _ in range(N+1)]
    for i in range(1,N+1):
        dp[i][0] = i
    for j in range(1,M+1):
        dp[0][j] = j
    for i in range(1, N+1):
        for j in range(1, M+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]+1, dp[i][j-1]+1)
            else:
                dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)
    # print(dp[N][M])
    # longest = []
    # i = N
    # j = M
    # while i > 0 and j > 0:
    #     if dp[i][j] > dp[i-1][j-1]:
    #         longest.append(A[i-1])
    #         i -= 1
    #         j -= 1
    #     elif dp[i][j] == dp[i-1][j]:
    #         i -= 1
    #     elif dp[i][j] == dp[i][j-1]:
    #         j -= 1
    #     else:
    #         # not reach
    #         pass
    # print(longest[::-1])
    print(dp[N][M])
            
if __name__ == '__main__':
    main()
