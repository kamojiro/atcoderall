#import sys
#input = sys.stdin.readline
from collections import defaultdict
def main():
    Q = 10**9+7
    N, M = map( int, input().split())
    S = list( map( int, input().split()))
    T = list( map( int, input().split()))
    dp = [ [1]*(M+1) for _ in range(N+1)]
    e = defaultdict( int)
    for i in range(N):
        e[S[i]] += 1
        d = defaultdict( int)
        for j in range(M):
            if S[i] == T[j]:
                dp[i+1][j+1] = (dp[i+1][j] + dp[i][j+1])%Q
            else:
                d[T[j]] += 1
                print()
                dp[i+1][j+1] = (max(dp[i+1][j], dp[i][j+1])+d[S[i]]*e[S[i]])%Q
    print( dp[N][M])
if __name__ == '__main__':
    main()
