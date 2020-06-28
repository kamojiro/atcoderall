#import sys
#input = sys.stdin.readline
def main():
    S = list( map( int, list( input())))
    N = len(S)
    dp = [[0,0] for _ in range(N+1)]
    dp[0][1] = 2
    for i in range(N):
        s = S[i]
        dp[i+1][0] = min(dp[i][0] + s, dp[i][1]+s)
        dp[i+1][1] = min(dp[i][0] + 11-s, dp[i][1]+9-s)
        # dp[i+1][2] = min(dp[i][1], dp[i][2])+9-s
        # 11-sは、追加で支払うものと、お釣り
        # 9-sは、追加はすでに支払われていて、繰り下がりが起こっている
    print( min(dp[N][0], dp[N][1]))
if __name__ == '__main__':
    main()
