#import sys
#input = sys.stdin.readline
def main():
    H, W = map( int, input().split())
    S = [ list( input()) for _ in range(H)]
    # if S[0][0] == "#":
    #     for i in range(H):
    #         for j in range(W):
    #             if S[i][j] == ".":
    #                 S[i][j] = "#"
    #             else:
    #                 S[i][j] = "."
    dp = [[10**5]*W for _ in range(H)]
    # if S[0][0] == "#":
    #     dp[0][0] = 1
    # else:
    #     dp[0][0] = 0
    dp[0][0] = 0
    for i in range(H):
        for j in range(W):
            if i > 0:
                if S[i-1][j] == S[i][j]:
                    if dp[i-1][j] < dp[i][j]:
                        dp[i][j] = dp[i-1][j]
                else:
                    if dp[i-1][j]+1 < dp[i][j]:
                        dp[i][j] = dp[i-1][j]+1
            if j > 0:
                if S[i][j-1] == S[i][j]:
                    if dp[i][j-1] < dp[i][j]:
                        dp[i][j] = dp[i][j-1]
                else:
                    if dp[i][j-1]+1 < dp[i][j]:
                        dp[i][j] = dp[i][j-1]+1
    #print(dp)
    ans = dp[H-1][W-1]
    ans //= 2
    if S[0][0] == "#" or S[H-1][W-1] == "#":
        ans += 1
    print(ans)
                
if __name__ == '__main__':
    main()
