#import sys
#input = sys.stdin.readline
def main():
    Q = 10**9+7
    N, M = map( int, input().split())
    S = list( map( int, input().split()))
    T = list( map( int, input().split()))
    dp = [ [0]*(M+1) for _ in range(N+1)]
    memo = [ [0]*(M+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(M):
            if S[i] == T[j]:
                dp[i+1][j+1] = (dp[i+1][j] + dp[i][j+1]+1)%Q
            else:
                dp[i+1][j+1] = (dp[i+1][j] + dp[i][j+1] - dp[i][j])%Q
    print(dp[N][M]+1)
if __name__ == '__main__':
    main()
