#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    S = list( input())
    dp = [[0]*7 for _ in range(N)]
    if S[0] == "R":
        dp[0][0] = 1
    elif S[0] == "G":
        dp[0][1] = 1
    else:
        dp[0][2] = 1
    for i in range(1,N):
        s = S[i]
        for j in range(7):
            dp[i][j] = dp[i-1][j]
        if s == "R":
            dp[i][0] += 1
            dp[i][3] += dp[i-1][1]
            dp[i][5] += dp[i-1][2]
            dp[i][6] += dp[i-1][4]
        elif s == "G":
            dp[i][1] += 1
            dp[i][3] += dp[i-1][0]
            dp[i][4] += dp[i-1][2]
            dp[i][6] += dp[i-1][5]
        else:
            dp[i][2] += 1
            dp[i][4] += dp[i-1][1]
            dp[i][5] += dp[i-1][0]
            dp[i][6] += dp[i-1][3]
    # print(dp)
    ans = dp[N-1][6]
    # for i in range(N):
    #     ans += dp[i][6]
    # print(ans)
    for d in range(1,N//2+1):
        for i in range(N-d*2):
            # print(d,i,i+2*d)
            if S[i] != S[i+d] and S[i] != S[i+2*d] and S[i+d] != S[i+2*d]:
                ans -= 1
    print(ans)

if __name__ == '__main__':
    main()
