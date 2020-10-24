#import sys
#input = sys.stdin.readline
# from itertools import accumulate
# from bisect import bisect_right
Q = 10**9+7
def main():
    N, K = map(int,input().split())
    V = [list(map(int,input().split())) for _ in range(N)]
    dp = [[1]*K, [0]*K]
    for i in range(1,N):
        # acc = list(accumulate(V[i-1]))
        before = (i-1)%2
        now = i%2
        index = 0
        acc = 0
        for j, v in enumerate(V[i]):
            while index < K:
                if v < V[i-1][index]: #v >= V[i-1]
                    break
                acc += dp[before][index]
                acc %= Q
                index += 1
            dp[now][j] = acc
        # print(before, dp[before])
        # print(now, dp[now])
    print(sum(dp[(N-1)%2])%Q)
if __name__ == '__main__':
    main()
