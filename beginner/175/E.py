#import sys
#input = sys.stdin.readline
def main():
    R, C, K = map( int, input().split())
    V = [[0]*C for _ in range(R)]
    for _ in range(K):
        r, c, v = map( int, input().split())
        V[r-1][c-1] = v
    dp0 = [[0]*(C+1) for _ in range(R+1)]
    dp1 = [[0]*(C+1) for _ in range(R+1)]
    dp2 = [[0]*(C+1) for _ in range(R+1)]
    dp3 = [[0]*(C+1) for _ in range(R+1)]
    for r in range(1,R+1):
        m = 0
        for c in range(1,C+1):
            m = max(m,dp0[r-1][c], dp1[r-1][c], dp2[r-1][c], dp3[r-1][c])
            dp0[r][c] = max(m, dp0[r][c-1])
            dp1[r][c] = max(dp1[r][c-1], dp0[r][c]+V[r-1][c-1])
            dp2[r][c] = max(dp2[r][c-1], dp1[r][c-1]+V[r-1][c-1])
            dp3[r][c] = max(dp3[r][c-1], dp2[r][c-1]+V[r-1][c-1])
    # print(dp0)
    # print(dp1)
    # print(dp2)
    # print(dp3)
    print( max( max(dp0[R]), max(dp1[R]), max(dp2[R]), max(dp3[R])))
if __name__ == '__main__':
    main()
