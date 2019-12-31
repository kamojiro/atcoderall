#import sys
#input = sys.stdin.readline
def main():
    N, K = map( int, input().split())
    rsp = list(map( int, input().split()))
    T = input()
    TmodK = [[] for _ in range(K)]
    for i in range(N):
        if T[i] == 'r':
            TmodK[i%K].append(0)
        elif T[i] == 's':
            TmodK[i%K].append(1)
        elif T[i] == 'p':
            TmodK[i%K].append(2)
    ans = 0
    cnt = N//K
    red = N%K
    s = 0
    for i in range(K):
        if i < red:
            s = 1
        else:
            s = 0
        dp = [[0,0,0] for _ in range(cnt+s)]
        dp[0][(TmodK[i][0] + 2)%3] = rsp[(TmodK[i][0] + 2)%3]
        for j in range(1, cnt+s):
            t = TmodK[i][j]

            win = (t+2)%3
            # print(t, win)
            for q in range(3):
                if q == win:
                    dp[j][q] = max(dp[j-1][(q+1)%3] + rsp[win], dp[j-1][(q+2)%3] + rsp[win])
                else:
                    dp[j][q] = max(dp[j-1][(q+1)%3], dp[j-1][(q+2)%3])
#        print(dp)
        ans += max(dp[cnt+s-1])
    print(ans)

if __name__ == '__main__':
    main()
