#import sys
#input = sys.stdin.readline
def main():
    X, Y = map( int, input().split())
    N = int( input())
    TH = [ tuple( map( int, input().split())) for _ in range(N)]
    dp = [[0]*(X+Y+1) for _ in range(X+1)]
    for t, h in TH:
        for x in range(X-1,-1,-1):
            for i in range(X+Y,t-1,-1):
                dp[x+1][i] = max(dp[x+1][i], dp[x][i-t]+h)
        # print(dp)
    print( max( [max(dp[i]) for i in range(X+1)]))

if __name__ == '__main__':
    main()
