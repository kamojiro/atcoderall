#import sys
#input = sys.stdin.readline
# from math import log10
def get_like(z):
    if z == 0:
        return 0
    N = len(str(z))
    dp = [[0]*N for _ in range(2)]
    C = []
    p = z
    while p > 0:
        C.append(p%10)
        p//=10
    B = C[::-1]
    y = B[0]
    if not (y == 9 or y == 4):
        dp[0][0] = 1
    if y == 9:
        dp[1][0] = 7
    elif y > 4:
        dp[1][0] = y-2
    elif y == 4:
        dp[1][0] = 3
    elif y > 0:
        dp[1][0] = y-1
    else:
        # no case
        pass
    
    for i, x in enumerate(B[1:]):
        if x == 9 or x == 4:
            dp[0][i+1] = 0
        else:
            dp[0][i+1] = dp[0][i]
        # 0..0a(a>0)
        dp[1][i+1] = 7
        # including 0
        if x == 9:
            dp[1][i+1] += dp[0][i]*8 + dp[1][i]*8
        elif x > 4:
            dp[1][i+1] += dp[0][i]*(x-1) + dp[1][i]*8
        elif x == 4:
            dp[1][i+1] += dp[0][i]*4 + dp[1][i]*8
        elif x > 0:
            dp[1][i+1] += dp[0][i]*x + dp[1][i]*8
        else:
            dp[1][i+1] += dp[1][i]*8
    # for a in dp:
    #     print(a)
    return z-(dp[0][N-1]+dp[1][N-1])

def main():
    A, B = map(int,input().split())
    # print(get_like(B))
    print(get_like(B)-get_like(A-1))
if __name__ == '__main__':
    main()
