#import sys
#input = sys.stdin.readline
Q = 10**9+7
def main():
    H, W = map(int, input().split())
    S = [ input() for _ in range(H)]
    Tate = [0]*W
    Naname = [0]*(H+W)
    dp = [[0]*W for _ in range(H)]
    dp[0][0] = 1
    now = 1
    Naname[0] = 1
    for j in range(1,W):
        if S[0][j] == "#":
            now = 0
            continue
        dp[0][j] = now
        Tate[j] = now
        Naname[j] = now
        now *= 2
        now %= Q
    now = 1
    for i in range(1,H):
        if S[i][0] == "#":
            now = 0
            continue
        dp[i][0] = now
        Naname[W+i] = now
        now *= 2
        now %= Q
    
    for i in range(1,H):
        yoko = dp[i][0]
        for j in range(1,W):
            if S[i][j] == "#":
                yoko = 0
                Tate[j] = 0
                if i <= j:
                    Naname[j-i] = 0
                else:
                    Naname[W+i-j] = 0
                continue
            dp[i][j] = yoko + Tate[j]
            if i <= j:
                dp[i][j] += Naname[j-i]
            else:
                dp[i][j] += Naname[W+i-j]
            dp[i][j] %= Q
            yoko += dp[i][j]
            yoko %= Q
            Tate[j] += dp[i][j]
            Tate[j] %= Q
            if i <= j:
                Naname[j-i] += dp[i][j]
                Naname[j-i] %= Q
            else:
                Naname[W+i-j] += dp[i][j]
                Naname[W+i-j] %= Q
    # print(dp)
    print(dp[H-1][W-1])
        
if __name__ == '__main__':
    main()
