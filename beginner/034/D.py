#import sys
#input = sys.stdin.readline
def main():
    N, K = map( int, input().split())
    W = [ tuple( map( int, input().split())) for _ in range(N)]
    dp = [[0,0] for _ in range(K+1)]
    dp[1][0] = W[0][0]
    dp[1][1] = W[0][0]*W[0][1]
    print(dp)
    for w, p in W[1:]:
        g = w*p
        for k in range(K,1,-1):
            if dp[k-1][0] == 0:
                continue
            if (dp[k-1][1] + g)*(dp[k][0]) >= dp[k][1]*(dp[k-1][0] + w):
                dp[k][0] = dp[k-1][0]+w
                dp[k][1] = dp[k-1][1] +g
            if g*(dp[1][0]) > dp[1][1]*w:
                dp[1][0] = w
                dp[1][1] = g
            print(dp)
    print( dp[K][1]/dp[K][0])
if __name__ == '__main__':
    main()
