#import sys
#input = sys.stdin.readline
def main():
    Q = 998244353
    N, K = map( int, input().split())
    LR = [ tuple( map( int, input().split())) for _ in range(K)]
    LR.sort()
    dp = [0]*(N+1)
    dp[1] = 1
    S = [0]*K
    for i in range(2,N+1):
        for j, (l, r) in enumerate(LR):
            if l <= i:
                S[j] += dp[i-l]
            if r < i:
                S[j] -= dp[i-r-1]
            S[j] %= Q
        dp[i] += sum(S)
        dp[i] %= Q
    # print(dp)
    print(dp[N])
    
if __name__ == '__main__':
    main()
