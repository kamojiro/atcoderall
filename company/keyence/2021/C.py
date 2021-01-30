#import sys
#input = sys.stdin.readline
def main():
    Q = 998244353
    H, W, K = map(int,input().split())
    B = [[0]*W for _ in range(H)]
    for _ in range(K):
        h, w, k = input().split()
        if k == "R":
            B[int(h)-1][int(w)-1] = 1
        elif k == "D":
            B[int(h)-1][int(w)-1] = 2
        else:
            B[int(h)-1][int(w)-1] = 3
    # print("a")
    waru3 = pow(3,Q-2,Q)
    dp = [[0]*W for _ in range(H)]
    dp[0][0] = 1
    if B[0][0] == 0:
        dp[0][0] = 3
    for j in range(1,W):
        if B[0][j-1] == 0:
            dp[0][j] = dp[0][j-1]*2%Q*waru3%Q
        elif B[0][j-1] == 1 or B[0][j-1] == 3:
            dp[0][j] = dp[0][j-1]
        if B[0][j] == 0:
            dp[0][j] *= 3
            dp[0][j] %= Q
    for i in range(1, H):
        # print(i)
        for j in range(W):
            d = 1
            r = 1
            if B[i-1][j] == 0:
                r = 3
            if j > 0:
                if B[i][j-1] == 0:
                    d = 3

            if B[i-1][j] == 0:
                dp[i][j] += dp[i-1][j]*2%Q*waru3%Q*d%Q
                # print(dp[i][j],dp[i-1][j],dp[i-1][j]*2%Q*waru3%Q*d%Q)
            elif B[i-1][j] == 2 or B[i-1][j] == 3:
                dp[i][j] += dp[i-1][j]*d%Q
            dp[i][j] %= Q
            if j > 0:
                if B[i][j-1] == 0:
                    dp[i][j] += dp[i][j-1]*2%Q*waru3%Q*r%Q
                elif B[i][j-1] == 1 or B[i][j-1] == 3:
                    dp[i][j] += dp[i][j-1]*r%Q
            dp[i][j] %= Q
            if B[i][j] == 0:
                dp[i][j] *= 3
            dp[i][j] %= Q
    # print(dp)
    print(dp[H-1][W-1]%Q)
if __name__ == '__main__':
    main()
