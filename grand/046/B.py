Q = 998244353
#import sys
#input = sys.stdin.readline
def main():
    A, B, C, D = map( int, input().split())
    dp = [[0]*3002 for _ in range(3001)]
    dp[C][D] = 1
    for a in range(C-1,A-1,-1):
        dp[a][D] = dp[a+1][D]*D%Q
    for b in range(D-1,B-1,-1):
        dp[C][b] = dp[C][b+1]*C%Q
    for a in range(C-1,A-1,-1):
        z = dp[a+1][D]*a%Q
        for b in range(D-1,B-1,-1):
            dp[a][b] = (b*dp[a+1][b] + z)%Q
            z = (z + dp[a+1][b])*a%Q
    # for i in range(C+1):
    #     print(dp[i][:D+1])
    print(dp[A][B])
if __name__ == '__main__':
    main()
