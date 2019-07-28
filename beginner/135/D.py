#import sys
#input = sys.stdin.readline
Q = 10**9+7
def main():
    S = input()
    N = len(S)
    dp = [[0]*13 for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        s = S[N-1-i]
        r = pow(10, i, 13)                
        if s == '?':
            for k in range(10):
                t = k*r%13
                for j in range(13):
                    dp[i+1][(j+t)%13] = (dp[i+1][(j+t)%13] + dp[i][j])%Q
            continue
        t = int(s)*r%13
        for j in range(13):
            dp[i+1][(j+t)%13] = dp[i][j]
    print(dp[N][5])
if __name__ == '__main__':
    main()
