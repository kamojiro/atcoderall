import sys
input = sys.stdin.readline
def main():
    H, N = map( int, input().split())
    AB = [ list( map( int, input().split())) for _ in range(N)]
    dp = [10**9]*H + [0]*(10**4+1)
    T = H+10**4
    for a, b in AB:
        for i in range(T,a-1,-1):
            if dp[i-a] > dp[i]+b:
                dp[i-a] = dp[i]+b
    print(dp[0])
if __name__ == '__main__':
    main()
