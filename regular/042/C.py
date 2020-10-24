import sys
input = sys.stdin.readline
def main():
    N, P = map(int,input().split())
    AB = [ tuple(map(int,input().split())) for _ in range(N)]
    AB.sort(reverse=True)
    dp = [0]*(P+1)
    ans = 0
    for a, b in AB:
        if ans < dp[P]+b:
            ans = dp[P]+b
        for i in range(P,a-1,-1):
            if dp[i] < dp[i-a]+b:
                dp[i] = dp[i-a]+b
    print(ans)
if __name__ == '__main__':
    main()
